from django.db import models

# Create your models here.
class Transport_Mem(models.Model):
  user=models.OneToOneField('Account.Custom',on_delete=models.CASCADE,unique=True,blank=True)
  name=models.CharField(max_length=40)
  email=models.EmailField(unique=True,max_length=60)
  phone_number=models.CharField(max_length=12)
  Driver_id=models.CharField(max_length=12)
  profile=models.ImageField(upload_to='Transport/Driver')
  Age=models.DateField()
  Address=models.CharField(max_length=60)

  def __str__(self):
    return f'{self.name}{self.email}{self.Address}'
  
class DailyDetail(models.Model):
  DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
  user=models.ForeignKey(Transport_Mem,on_delete=models.CASCADE,blank=True)
  Total_passenger=models.PositiveIntegerField()
  Total_student=models.PositiveIntegerField()
  Total_faculty=models.PositiveIntegerField()
  Day=models.CharField(choices=DAYS_OF_WEEK)
  Bus_Plate_number=models.CharField(max_length=10)
  date=models.DateField(auto_now=True)

  def __str__(self):
    return f'{self.Total_passenger}{self.Bus_Plate_number}'


