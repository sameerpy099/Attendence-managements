from django import forms
from .models import Facultyman
import re

class customfaculty(forms.ModelForm):
  class Meta:
   model=Facultyman
   fields=['Name','Email','profile_image','Department','positions','experience','Branch','Course']
   widgets={
     'Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),
     'Email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
     'profile_image':forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'profile image '}),
     'positions':forms.TextInput(attrs={'class':'form-control','placeholder':'positions '}),
     'experience':forms.TextInput(attrs={'class':'form-control','placeholder':'Work Experience '}),
     'Course':forms.Select(attrs={'class':'form-control'}),
     'Branch':forms.Select(attrs={'class':'form-control'}),
   }

  def clean_Email(self):
      Email = self.cleaned_data.get('Email')
      if not Email:
            raise forms.ValidationError("Email is required.")
      if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', Email):
            raise forms.ValidationError("Enter a valid email address.")
      if Facultyman.objects.filter(Email=Email).exists():
            raise forms.ValidationError("This email is already registered.")
      return Email
