# Generated by Django 4.2.7 on 2023-11-28 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('Opportunities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
        ),
    ]