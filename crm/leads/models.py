from django.db import models
from servicecrm.models import AccountUser

class Lead(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Qualified', 'Qualified'),
        ('Lost', 'Lost'),
        ('Converted', 'Converted'),
    ]
    
    SOURCE_CHOICES = [
        ('Website', 'Website'),
        ('Referral', 'Referral'),
        ('Advertisement', 'Advertisement'),
        ('Other', 'Other'),
    ]

    # Basic lead details
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    
    # Lead status and source
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    
    # Lead assignment and ownership
    assigned_to = models.ForeignKey(AccountUser, related_name='assigned_leads', on_delete=models.CASCADE)
    created_by = models.ForeignKey(AccountUser, related_name='created_leads', on_delete=models.CASCADE)

    # Additional lead details
    lead_description = models.TextField(blank=True, null=True)
    lead_score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
