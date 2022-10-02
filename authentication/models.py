from email.policy import default
from random import choices
from secrets import choice
from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Profile(models.Model):

  MALE='male'
  FEMALE='female'
  AUTHOR='Author'

  CHOICES=((MALE,'Male'),(FEMALE,"Female"),(AUTHOR,"Author"))

  user=models.OneToOneField(User,on_delete=models.CASCADE)
  first_name=models.CharField(max_length=256)
  last_name=models.CharField(max_length=256)
  gender=models.CharField(max_length=6,choices=CHOICES,default=AUTHOR)
  image=models.ImageField(upload_to="img/")
  phone_number=models.IntegerField(default=000000000,blank=True,null=True)

  def __str__(self) -> str:
    return self.user
  
  class Meta:
    db_table='profile'
