# Generated by Django 4.2.7 on 2023-11-28 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_cases', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='case',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_cases', to=settings.AUTH_USER_MODEL),
        ),
    ]
