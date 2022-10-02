from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from authentication.forms import ProfileUpdateForm

def home(request):
  return render(request,'index.html')

def login_view(request):

  if request.user.is_authenticated:
    return redirect("home")


  username=str(request.GET.get("username")).lower()
  password=request.GET.get("password")
  print(username,password)
  try:
    user=User.objects.get(username=username)
    print(user)
  except:
    messages.error(request,'User does not exist')
  user=authenticate(request,username=username,password=password)
  print(user)
  if user is not None:
    users=login(request,user)
    return redirect("home")

  return render(request, "auth/login.html")

def logout_user(request):
  logout(request)
  return redirect("home")


def register_view(request):

  if request.method=="POST":
    username=str(request.POST.get("username")).lower()
    email=request.POST.get("email")
    password1=request.POST.get("pass1")
    password2=request.POST.get("pass2")
    if password1==password2 and username is not None:
      users=User(username=username,email=email,password=password1)
      if users is not None:
        users.username=users.username.lower()
        users.save()
        login(request, users)
      return redirect("login")
  return render(request, "auth/register.html")

login_required
def change_password(request):
  if request.method=="POST":
    form = PasswordChangeForm(request.user,request.POST)
    if form.is_valid():
      user=form.save()
      update_session_auth_hash(request,user)
      messages.success(request, 'Your password was successfully updated!')
      return redirect("change_password")
    else:
      messages.error(request, 'Please correct the error below.')
  else:
    form=PasswordChangeForm(request.user)
  return render(request,'auth/change_password.html',{"form":form})



@login_required
def profile(request):
  if request.method=="POST":
    p_user=get_object_or_404(User,pk=request.user.id)
    p_user.username=request.POST.get("username")
    p_user.email=request.POST.get("email")
    p_user.password=request.POST.get("password")
    p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

    if p_form.is_valid() and p_user is not None:
      p_user.save()
      p_form.save()
      return redirect("profile")
  else:
    p_user=get_object_or_404(User,pk=request.user.id)
    p_form=ProfileUpdateForm(instance=request.user.profile)
  return render(request,"profile.html",{"p_user":p_user,"p_form":p_form})

