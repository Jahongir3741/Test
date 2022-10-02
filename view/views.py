from django.shortcuts import render
from view.models import Test_Q, Question,Answers

def tests_q(request):
  test=Test_Q.objects.all()
  return render(request,'view/test.html',{"test":test})

def quetion(request,pk):
  test=Test_Q.objects.get(id=pk)
  quetion=Question.objects.filter(tests=test.id)
  answer=Answers.objects.()
  ans=Answers.objects.filter(quetions=answer.id)  
  context={"ques":quetion,"answer":ans}
  return render(request,'view/ques.html',context)

