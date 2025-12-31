from django.db import models
from django.contrib.auth.models import User

class LibrarianDetail(models.Model):
  course=[
    ('Btech','Btech'),
    ('Management','Management'),
    ('Bsc Agricuture','Bsc Agriculture'),
    ('BSC Nursing','Bsc Nursing'),
    ('BCA','BCA'),
    ( 'LAW','LAW'),
    ('MCA','MCA'),
    ('Mtech','Mtech'),
    ('MBBS','MBBS'),
    ( 'Art Science','Art Science'),
      ]
    
  name=models.CharField(max_length=30)
  user=models.OneToOneField('Account.Custom',on_delete=models.CASCADE,blank=True)
  Librarian_Id=models.CharField(max_length=12)
  Course=models.CharField(choices=course)
  Library_id=models.CharField(max_length=10)
  No_of_department=models.CharField(max_length=12)


  def __str__(self):
    return '{self.name}{self.Librarian_Id}{self.Course}'
  

class AddeRecordLibrary(models.Model):
  DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
  Books=models.CharField(max_length=12)
  Total_Student=models.CharField(max_length=12)
  Total_System=models.CharField(max_length=12)
  Day=models.CharField(choices=DAYS_OF_WEEK)

