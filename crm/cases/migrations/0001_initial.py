# Generated by Django 4.2.7 on 2023-11-28 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('priority', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=10)),
                ('status', models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved'), ('Closed', 'Closed')], default='New', max_length=20)),
                ('resolution_notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]