from urllib.parse import urlparse
from django.urls import path
from authentication.views import \
   login_view,register_view,home,logout_user,profile,change_password

urlpatterns = [
  path('login/',login_view,name="login"),
  path('register/',register_view,name="register"),
  path('logout/',logout_user,name='logout'),
  path('password/',change_password,name='change_password'),
  path('profile/',profile,name="profile"),
  path('',home,name='home'),
]
