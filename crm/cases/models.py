from django.db import models
from servicecrm .models import AccountUser

class Case(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]
    
    # Basic case details
    case_title = models.CharField(max_length=200)
    description = models.TextField()
    
    # Case priority and status
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    
    # Assignment and ownership
    # assigned_to = models.ForeignKey(AccountUser, on_delete=models.SET_NULL, null=True, blank=True)
    # created_by = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(AccountUser, related_name='assigned_cases', on_delete=models.CASCADE)
    created_by = models.ForeignKey(AccountUser, related_name='created_cases', on_delete=models.CASCADE)
    
    # Resolution logs and tracking
    resolution_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.case_title
