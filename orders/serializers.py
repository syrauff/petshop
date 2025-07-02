from rest_framework import serializers
from django.utils import timezone
from .models import Booking, ClinicAppointment, GroomingBooking
from pets.serializers import PetSerializer
from users.serializers import UserSimpleSerializer

class BookingSerializer(serializers.ModelSerializer):
    pet = PetSerializer(read_only=True)
    user = UserSimpleSerializer(read_only=True)
    pet_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'pet', 'pet_id', 'start_date', 'end_date', 'status', 'notes', 'created_at']
        read_only_fields = ['user', 'status']
        
class ClinicAppointmentSerializer(serializers.ModelSerializer):
    pet = PetSerializer(read_only=True)
    user = UserSimpleSerializer(read_only=True)
    pet_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ClinicAppointment
        fields = ['id', 'user', 'pet', 'pet_id', 'appointment_datetime', 'reason', 'status', 'doctor_notes', 'created_at']
        read_only_fields = ['user', 'status', 'doctor_notes']

        def validate(self, value):
            if value < timezone.now():
                raise serializers.ValidationError("Appointment datetime cannot be in the past.")
            
            return value

class GroomingBookingSerializer(serializers.ModelSerializer):
    pet = PetSerializer(read_only=True)
    user = UserSimpleSerializer(read_only=True)
    pet_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = GroomingBooking
        fields = ['id', 'user', 'pet', 'pet_id', 'service_type', 'appointment_datetime', 'status', 'created_at']
        read_only_fields = ['user', 'status']

        def validate(self, value):
            if value < timezone.now():
                raise serializers.ValidationError("Appointment datetime cannot be in the past.")
            
            return value
        
        