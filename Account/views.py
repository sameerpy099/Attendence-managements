from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# faculty registrations view here 

def customlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirect based on role
            if user.Role == 'Student':
                return redirect('studentdashboard')
            elif user.Role == 'Faculty':
                return redirect('faculty_dashboard')
            elif user.Role == 'TransportMem':
                return redirect('transportdashboard')
            else:
                messages.error(request, "Invalid Role assigned.")
                return redirect('loginpage')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('loginpage')

    # If GET request, show the login page
    return render(request, 'login.html')

def Logout_page(request):
  logout(request)
  return redirect ('loginpage')


