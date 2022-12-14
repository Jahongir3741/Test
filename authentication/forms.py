from django.forms import ModelForm
from authentication.models import Profile

class ProfileUpdateForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['first_name','last_name','gender','image','phone_number']