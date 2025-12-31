from django.db import models

# Create your models here.
class student_basic_detail(models.Model):
  STATE_CHOICES = [
        # --- States ---
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CT', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OD', 'Odisha'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TG', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal'),

        # --- Union Territories ---
        ('AN', 'Andaman and Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DN', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('DL', 'Delhi'),
        ('JK', 'Jammu and Kashmir'),
        ('LA', 'Ladakh'),
        ('LD', 'Lakshadweep'),
        ('PY', 'Puducherry'),
    ]
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
  student_id=models.CharField(max_length=12,blank='',null=True)
  first_name=models.CharField(max_length=50,blank="",null=True)
  last_name=models.CharField(max_length=50,blank="",null=True)
  mother_name=models.CharField(max_length=50)
  father_name=models.CharField(max_length=50)
  Permanent_address=models.CharField(max_length=50)
  state=models.CharField(choices=STATE_CHOICES,max_length=50,default="Select State")
  pin_code=models.IntegerField(null=True,blank=True)
  local_address=models.CharField(max_length=80)

  profile_image=models.ImageField(upload_to='student/images/')
  signature=models.ImageField(upload_to='student/signature/')
  mobile_number=models.CharField(max_length=12 ,unique=True)
  email=models.EmailField(max_length=50,unique=True)
  blood_group=models.CharField(max_length=5)
  pancard_number=models.CharField(max_length=12)


  High_marksheet=models.FileField(upload_to='student/document/')
  Inter_marksheet=models.FileField(upload_to='student/document/')
  Migrations=models.FileField(upload_to='student/document/')
  Character_cirtificate=models.FileField(upload_to='student/document/')
  TC=models.FileField(upload_to='student/document/')
  Aadhar=models.FileField(upload_to='student/document/')

  high_passout = models.CharField(max_length=30,blank="2000",null=True)
  inter_passout = models.CharField(max_length=30,blank="2000",null=True)
  high_percentage = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
  inter_percentage = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)

  Course=models.CharField(choices=course ,max_length=50,default="Select Course")
  Branch=models.CharField(choices=branch ,max_length=80 ,default="Select Branch")
  Dob=models.DateField()

  def __str__(self):
    return f'{self.Branch} {self.course}'



