from django.db import models
from django.db import models
from accounts.models import Account  # Import the Account model if it's in a different app


class Contact(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    # Basic contact details
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birth_date = models.DateField(null=True, blank=True)

    # Relationship with account
    # account = models.ForeignKey('Account', on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    # Communication preferences
    preferred_contact_method = models.CharField(max_length=20)
    do_not_contact = models.BooleanField(default=False)

    # Additional fields
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)

    # Communication logs or history (could be a separate model)
    # communication_logs = ForeignKey/Many-to-Many relation with CommunicationLogs model

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
