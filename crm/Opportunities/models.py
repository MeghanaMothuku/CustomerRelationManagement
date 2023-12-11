from django.db import models
from accounts.models import Account
from leads.models import Lead

class Opportunity(models.Model):
    STAGE_CHOICES = [
        ('Prospecting', 'Prospecting'),
        ('Qualification', 'Qualification'),
        ('Proposal', 'Proposal'),
        ('Negotiation', 'Negotiation'),
        ('Closed - Won', 'Closed - Won'),
        ('Closed - Lost', 'Closed - Lost'),
    ]

    # Basic opportunity details
    opportunity_name = models.CharField(max_length=150)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    
    # Opportunity stage and probability
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES)
    probability = models.PositiveIntegerField(default=0, help_text='Probability of closing in percentage')

    # Sales and financial details
 
