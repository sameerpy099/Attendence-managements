from django.shortcuts import render,redirect
from Account.utils import generate_unique_transport_id,generate_random_password
from .transportform import CustomTransport
from .passengerform import Custompassenger
from django.contrib.auth.hashers import make_password
from Account.models import Custom
from .models import Transport_Mem,DailyDetail
from datetime import date
from Account.utilsemail import Email_send
# Create your views here.
def TranspotDriver(request):
   if request.method=="POST":
      form=CustomTransport(request.POST,request.FILES)
      if form.is_valid():
         Role='TransportMem'
         email = form.cleaned_data["email"]
         name = form.cleaned_data["name"]
         username=generate_unique_transport_id()
         password=generate_random_password()

         user=Custom.objects.create(
            username=username,
            password=make_password(password),
            Role='TransportMem',
         )

         transportprofile=form.save(commit=False)
         transportprofile.user=user
         transportprofile.Driver_id=username
         transportprofile.save()
         
         Email_send(email,username,Role,name,password)
         
         return render(request,'registration_success.html',{'student_id': username,'password': password})
      return render(request,'transportmemform.html',{'form':form})
   else:
      form=CustomTransport()
      return render(request,'transportmemform.html',{'form':form})
   
   
def PassengerDetail(request):
    Transport_user = Transport_Mem.objects.get(user=request.user)
    Today = date.today()


    already_submit = DailyDetail.objects.filter(user=Transport_user, date=Today).exists()

    if request.method == 'POST':

        if already_submit:
            return render(request, 'TransportDetail.html', {
                'form': Custompassenger(),
                'already': True,
                'message': 'Aap aaj ke liye detail pehle hi submit kar chuke hain.'
            })

        form = Custompassenger(request.POST)
        if form.is_valid():
            Driverprofile = form.save(commit=False)
            Driverprofile.user = Transport_user
            # no need to set date manually because model auto adds it
            Driverprofile.save()
            
            return redirect('transportdashboard')

        return render(request, 'TransportDetail.html', {'form': form, 'already': already_submit})

    else:
        form = Custompassenger()
        return render(request, 'TransportDetail.html', {'form': form, 'already': already_submit})

def TranspotDriverDashboard(request):
   form=Transport_Mem.objects.get(user=request.user)
   return render(request,'Driverdashboard.html',{'form':form})


def history(request):
    user=Transport_Mem.objects.get(user=request.user)
    Alldetail=DailyDetail.objects.filter(user=user).order_by('-date')
    return render(request,'history.html',{'user':user,'Alldetail':Alldetail})

def report(request):
    return render(request,'report.html')