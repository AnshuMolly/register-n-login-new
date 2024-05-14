from django.db import models

def default_address():
    return "123 Main Street"  # Your default address

def default_phone_number():
    return "123-456-7890"  # Your default phone number

def default_pincode():
    return "000000"  # Your default pin code

def default_email():
    return "example@example.com"  # Your default email address

class Service(models.Model):
    service_username = models.CharField(max_length=50)
    service_password = models.CharField(max_length=30)
    email = models.EmailField(default=default_email)  # Set the default email here
    phone_number = models.CharField(max_length=15, default=default_phone_number)  # Set the default value here
    address = models.CharField(max_length=100, default=default_address)  # Set the default value here
    pincode = models.CharField(max_length=10, default=default_pincode)  # Set the default value here
