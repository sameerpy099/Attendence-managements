from django.shortcuts import render,redirect
from Account.models import Custom
from django.contrib.auth.hashers import make_password
from Account.utils import generate_random_password,generate_unique_student_id
from .studentform import CustomRegistration
from .models import student_basic_detail
from Account.utilsemail import Email_send

def registration_mode(request):
  if request.method == "GET" and request.user.is_authenticated:
      return redirect('loginpage')
  
  if request.method=="POST":
   form=CustomRegistration(request.POST, request.FILES)
   if form.is_valid():
     email=form.cleaned_data['email']
     name=form.cleaned_data['name']
     Role='Student'
     username=generate_unique_student_id()
     password=generate_random_password()

     user=Custom.objects.create(
       username=username,
       password=make_password(password),
       Role='Student'
     )
     profile=form.save(commit=False)
     profile.user=user
     profile.student_id = username
     profile.save()
     
     Email_send(email,username,Role,name,password)
      
     return render(request, 'registration_success.html', {
                'student_id': username,
                'password': password
            })
   
   return render(request,'registration.html',{'form':form})
  else:

    form=CustomRegistration() 
    return render(request,'registration.html',{'form':form})
  
def studentdef(request):
  user=request.user
  profile=student_basic_detail.objects.get(user=user)
  return render(request,'studentdashboard.html',{'profile':profile})

def studentprofile(request):
  student = student_basic_detail.objects.get(user=request.user)
  return render(request, 'profile.html', {'student': student})