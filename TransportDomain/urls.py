from django.urls import path
from .import views
urlpatterns=[
  path('transportpage/form',views.TranspotDriver,name='transportpage'),
  path('transportdashboard/Drivers',views.TranspotDriverDashboard,name='transportdashboard'),
  path('Trabnsport/Passenger',views.PassengerDetail,name='Passengerdetail'),
  path('Trabnsport/Passenger/detail',views.history,name='history'),
  path('Trabnsport/Passenger/report',views.report,name='Passengerreport'),
]