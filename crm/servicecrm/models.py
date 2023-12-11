from django.db import models
from django.contrib.auth.models import AbstractUser


class AccountUser(AbstractUser):
    username=models.CharField(unique=True,max_length=100)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20, null=True)





    


    
    

