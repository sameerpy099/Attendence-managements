from django.urls import path
from . import views
urlpatterns=[
  path('faculty_reg/faculty-form!',views.faculty_reg,name='facultyreg'),
  path('faculty/faculty_Dashbopard!',views.Faculty_dashboard,name='faculty_dashboard'),
]