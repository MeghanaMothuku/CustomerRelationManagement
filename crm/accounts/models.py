from django.db import models
from servicecrm.models import AccountUser


class Account(models.Model):
    # Basic account details
    account_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=50)
    account_owner = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Contact information
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)

    # Billing information
    billing_address = models.TextField()
    billing_city = models.CharField(max_length=50)
    billing_state = models.CharField(max_length=50)
    billing_country = models.CharField(max_length=50)
    billing_postal_code = models.CharField(max_length=20)

    # Additional fields
    account_description = models.TextField(blank=True, null=True)
    account_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.account_name


