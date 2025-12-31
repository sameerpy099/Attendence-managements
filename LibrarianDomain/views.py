from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def home(request):
  send_mail(
    "Student Registration Confirmations",
    "Student id : ST000001233  Password: ST000WGHSBT",
    "codinguse79@gmail.com",
    ["dsd038234@gmail.com"],
    fail_silently=False,
)
  return render(request,'homr.html')