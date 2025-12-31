from django.urls import path
from. import views

urlpatterns=[
  path("Attendece/RecordSubmit",views.Record_list,name='Record_attendance'),
  
]