from django.shortcuts import render
from Student.models import student_basic_detail


def base(request):
  form=student_basic_detail.objects.filter(user=request.user).first()
  return render(request,'components/base.html',{'form':form})


def homepage(request):
  return render(request,'index.html')
def update(request):
  return render(request,'update.html')
