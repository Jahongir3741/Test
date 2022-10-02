from django.urls import path
from view.views import tests_q,quetion

urlpatterns = [
  path('test/',tests_q,name="test"),
  path('ques/<int:pk>/',quetion,name="question"),
]
