from django.db import models

from django.contrib.auth.models import AbstractUser

class Custom(AbstractUser):
  role=[
    ('Student','Student'),
    ('Faculty','Faculty'),
    ('Admin','Admin'),
    ('TransportMem','TransportMem'),
  ]
  Role=models.CharField(choices=role)



  






  
