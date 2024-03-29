# Generated by Django 4.2.7 on 2023-11-28 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('Contacted', 'Contacted'), ('Qualified', 'Qualified'), ('Lost', 'Lost'), ('Converted', 'Converted')], default='New', max_length=20)),
                ('source', models.CharField(choices=[('Website', 'Website'), ('Referral', 'Referral'), ('Advertisement', 'Advertisement'), ('Other', 'Other')], max_length=20)),
                ('lead_description', models.TextField(blank=True, null=True)),
                ('lead_score', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
