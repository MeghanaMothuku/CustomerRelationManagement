from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from accounts.models import Account
from contacts.models import Contact
from leads.models import Lead


@receiver(post_migrate)
def create_permissions(sender, **kwargs):
    if sender.name == 'servicecrm':  # Replace 'users' with the name of your users app
        content_type_account = ContentType.objects.get_for_model(Account)
        content_type_contact = ContentType.objects.get_for_model(Contact)
        content_type_lead = ContentType.objects.get_for_model(Lead)
        
        # Permissions for Account
        Permission.objects.get_or_create(
            codename='can_access_account',
            name='Can Access Account',
            content_type=content_type_account,
        )
        
        # Permissions for Contact
        Permission.objects.get_or_create(
            codename='can_access_contact',
            name='Can Access Contact',
            content_type=content_type_contact,
        )
        
        # Permissions for Lead
        Permission.objects.get_or_create(
            codename='can_access_lead',
            name='Can Access Lead',
            content_type=content_type_lead,
        )