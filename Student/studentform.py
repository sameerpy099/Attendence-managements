from django import forms
from .models import student_basic_detail
import re
class CustomRegistration(forms.ModelForm):
  class Meta:
    model=student_basic_detail
    fields=['first_name','last_name','Dob','mother_name','father_name','Permanent_address','local_address','state','pin_code','mobile_number','email','blood_group','pancard_number','high_passout','inter_passout','high_percentage','inter_percentage','Course','Branch','profile_image','signature','High_marksheet','Inter_marksheet','Migrations','Character_cirtificate','TC','Aadhar']
    widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'Dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mother’s Name'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Father’s Name'}),
            'Permanent_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Permanent Address'}),
            'local_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Local Address'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'pin_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PIN Code'}), 
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10-digit Mobile Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'blood_group': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., A+, O+'}),
            'pancard_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PAN Number'}),

            'high_passout': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'High School Year'}),
            'inter_passout': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Intermediate Year'}),
            'high_percentage': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'High School %'}),
            'inter_percentage': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Intermediate %'}),
            'Course': forms.Select(attrs={'class': 'form-select'}),
            'Branch': forms.Select(attrs={'class': 'form-select'}),

            'profile_image':forms.ClearableFileInput(attrs={'class':'image-input'}),
            'signature':forms.ClearableFileInput(attrs={'class':'image-input'}),
            'High_marksheet':forms.ClearableFileInput(attrs={'class':'image-input'}),
            'Inter_marksheet':forms.ClearableFileInput(attrs={'class':'image-input'}),
            'Migrations':forms.ClearableFileInput(attrs={'class':'image-input'}),
            'Character_cirtificate':forms.ClearableFileInput(attrs={'class':'image-input'}),
            'TC':forms.ClearableFileInput(attrs={'class':'image-input'}),
            'Aadhar':forms.ClearableFileInput(attrs={'class':'image-input'}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise forms.ValidationError("Enter a valid email address.")
        return email

    def clean_mobile_number(self):
        mobile = self.cleaned_data.get('mobile_number')
        if not mobile:
            raise forms.ValidationError("Mobile number is required.")
        if not re.match(r'^[6-9]\d{9}$', mobile):
            raise forms.ValidationError("Enter a valid 10-digit Indian mobile number starting with 6, 7, 8, or 9.")
        return mobile

    def clean(self):
        cleaned_data = super().clean()
        file_type=['profile_image','signature','High_makrsheet','Inter_makrsheet','Migrations','Character_cirtificate','TC','Aadhar']

        max_size_of_file= 5*1024*1024
        for field in file_type:
           file=cleaned_data.get(field)
           if file:
              valid_types=['applications/pdf','image/jpeg','image/png']
              if file.content_type not in valid_types:
                 raise forms.ValidationError("images not allow except pdf png image applications ")
           if file.size>max_size_of_file:
              raise forms.ValidationError("File size not more than 5MB") 
           
        return cleaned_data
