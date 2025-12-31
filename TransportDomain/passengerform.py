from .models import DailyDetail
from django import forms

class Custompassenger(forms.ModelForm):
  class Meta:
    model=DailyDetail
    fields=['Total_passenger','Total_student','Total_faculty','Day','Bus_Plate_number']
    widgets={
      'Total_passenger':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Passenger'}),
      'Total_student':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Student Passenger'}),
      'Total_faculty':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Faculty Passenger'}),
      'Bus_Plate_number':forms.TextInput(attrs={'class':'form-control','placeholder':'UK07HE1234'}),
    }
    