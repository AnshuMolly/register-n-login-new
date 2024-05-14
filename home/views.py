
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Service
from django.db.utils import IntegrityError
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

  # Import the User model

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Service

def register(request):
    if request.method == 'POST':
        username = request.POST.get('loginname')
        password = request.POST.get('keyword')
        confirm_password = request.POST.get('confirm_password')  # Get confirm password
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')

        if password != confirm_password:  # Check if passwords match
            messages.error(request, "Passwords do not match.")
            return redirect('register')  # Redirect back to registration page with error message
        
        # Create a new user
        user = User.objects.create_user(username=username, password=password, email=email)

        # Create or update Service instance
        service_instance, created = Service.objects.get_or_create(service_username=username)
        service_instance.service_password = password
        service_instance.email = email
        service_instance.phone_number = phone_number
        service_instance.address = address
        service_instance.pincode = pincode
        service_instance.save()

        # Redirect to the login page after successful registration
        return redirect('login')

    return render(request, 'register.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to the 'index' URL
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
