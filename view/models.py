from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Test_Q(models.Model):
  user=models.ManyToManyField(User)
  name=models.CharField(max_length=512)
  start_time=models.DateTimeField(auto_now_add=True)
  # end_time=models.DateTimeField(auto_add=True)

  class Meta:
    db_table='test'
  
  def __str__(self) -> str:
    return self.name

class Question(models.Model):
  tests=models.ForeignKey(Test_Q,on_delete=models.CASCADE)
  q_name=models.CharField(max_length=1024)

  def __str__(self) -> str:
    return self.q_name

class Answers(models.Model):
  quetions=models.ForeignKey(Question,on_delete=models.CASCADE)
  a_name=models.CharField(max_length=512)
  answer=models.BooleanField(default=False)

  def __str__(self) -> str:
    return self.a_name


