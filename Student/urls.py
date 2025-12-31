from django.urls import path
from .import views
urlpatterns=[
  path('',views.studentdef,name='studentdashboard'),
  path('Student/Studentprofile/profile',views.studentprofile,name='studentprofile'),
  path('Student/Registration!@',views.registration_mode,name='registrationpage'),
]