from django.shortcuts import render
from Account.models import Custom
from Account.utils import generate_unique_Faculty_id,generate_random_password
from django.contrib.auth.hashers import make_password
from .facultyform import customfaculty
from Account.utilsemail import Email_send
# Create your views here.
def faculty_reg(request):
  if request.method=="POST":
     form=customfaculty(request.POST,request.FILES)
     if form.is_valid():
        Email = form.cleaned_data["Email"]
        Name = form.cleaned_data["Name"]
        username=generate_unique_Faculty_id()
        password=generate_random_password()
        Role="Faculty Of Department"

        user=Custom.objects.create(
           username=username,
           password=make_password(password),
           Role='Faculty',
        )

        Faculty_profile=form.save(commit=False)
        Faculty_profile.user=user
        Faculty_profile.faculty_id=username
        Faculty_profile.save()
        
      #   Registration email 
        Email_send(Email,username,Role,Name,password)
        
        return render(request,'registration_success.html',{'student_id': username,'password': password})
     
     return render(request,'facultyreg.html',{'form':form})
  else:
     form=customfaculty()
     return render(request,'facultyreg.html',{'form':form})

def Faculty_dashboard(request):
   return render(request,'dashboard.html')