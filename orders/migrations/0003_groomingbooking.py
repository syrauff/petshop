# Generated by Django 5.2.2 on 2025-06-24 13:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_clinicappointment'),
        ('pets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroomingBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('bathing', 'Bathing'), ('haircut', 'Haircut'), ('nail_clipping', 'Nail Clipping'), ('full_grooming', 'Full Grooming')], default='bathing', max_length=20)),
                ('appointment_datetime', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=10)),
                ('notes', models.TextField(blank=True, help_text='Additional notes for the grooming service', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grooming_bookings', to='pets.pet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grooming_bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
