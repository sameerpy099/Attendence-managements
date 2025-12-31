from django.db import models

# Create your models here.
class Facultyman(models.Model):
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
  branch=[
        ('CSE', 'Computer Science and Engineering'),
        ('IT', 'Information Technology'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('AE', 'Automobile Engineering'),
        ('CHE', 'Chemical Engineering'),
        ('BT', 'Biotechnology'),
        ('AERO', 'Aerospace Engineering'),
        ('MIN', 'Mining Engineering'),
        ('MT', 'Metallurgical Engineering'),
        ('DS', 'Data Science'),
        ('AI', 'Artificial Intelligence & Machine Learning'),
        ('IOT', 'Internet of Things'),
        ('ROBO', 'Robotics and Automation'),
        ('ENV', 'Environmental Engineering'),
        ('MBBS', 'Bachelor of Medicine, Bachelor of Surgery'),
        ('BDS', 'Bachelor of Dental Surgery'),
        ('BPT', 'Bachelor of Physiotherapy'),
        ('BPHARM', 'Bachelor of Pharmacy'),
        ('NURS', 'Nursing'),
        ('BSC', 'Bachelor of Science'),
        ('MSC', 'Master of Science'),
        ('BSTAT', 'Bachelor of Statistics'),
        ('BCOM', 'Bachelor of Commerce'),
        ('MCOM', 'Master of Commerce'),
        ('BBA', 'Bachelor of Business Administration'),
        ('MBA', 'Master of Business Administration'),
        ('BBM', 'Bachelor of Business Management'),
        ('BSC_AGRI', 'B.Sc Agriculture'),
        ('BSC_HORT', 'B.Sc Horticulture'),
        ('BSC_FOREST', 'B.Sc Forestry'),
   ]
  user = models.OneToOneField('Account.Custom', on_delete=models.CASCADE, null=True, blank=True)
  faculty_id=models.CharField(max_length=12,blank='True', null=True)
  Name=models.CharField(max_length=30)
  Email=models.EmailField(max_length=30)
  profile_image=models.ImageField(upload_to='Facultymanage/faculty/')
  Department=models.CharField(max_length=23)
  positions=models.CharField(max_length=30)
  experience=models.CharField(max_length=10)
  Course=models.CharField(choices=course ,max_length=50,default="Select Corse")
  Branch=models.CharField(choices=branch ,max_length=80,default="Select Branch")

  def __str__(self):
    return f'{self.Name} - {self.Department} - {self.positions}'
