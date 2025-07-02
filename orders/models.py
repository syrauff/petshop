from django.db import models
from django.contrib.auth.models import User
from pets.models import Pet
# Create your models here.
class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True, null=True, help_text="Additional notes for the booking")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.pet.name} by {self.user.username} from {self.start_date} to {self.end_date}"
    
class ClinicAppointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clinic_appointments')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='clinic_appointments')
    appointment_datetime = models.DateTimeField()
    reason = models.CharField(max_length=255, help_text="Reason for the appointment")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')
    doctor_notes = models.TextField(blank=True, null=True, help_text="Notes from the veterinarian")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Janji temu untuk {self.pet.name} oleh {self.user.username} pada {self.appointment_datetime} - Status: {self.status}"
    
class GroomingBooking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    SERVICE_CHOICES = [
        ('bathing', 'Bathing'),
        ('haircut', 'Haircut'),
        ('nail_clipping', 'Nail Clipping'),
        ('full_grooming', 'Full Grooming'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grooming_bookings')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='grooming_bookings')
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES, default='bathing')
    appointment_datetime = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True, null=True, help_text="Additional notes for the grooming service")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Grooming ({self.get_service_type_display()}) untuk {self.pet.name} pada {self.appointment_datetime}"