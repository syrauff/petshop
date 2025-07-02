from django.shortcuts import render
from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Booking, ClinicAppointment, GroomingBooking
from .serializers import BookingSerializer, ClinicAppointmentSerializer, GroomingBookingSerializer
from pets.models import Pet

# Create your views here.
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        pet_id = self.request.data.get('pet_id')
        pet_to_book = Pet.objects.get(id=pet_id)
        if pet_to_book.owner != self.request.user:
            raise PermissionDenied("You can only book your own pets.")
        
        serializer.save(user=self.request.user, pet=pet_to_book)

class ClinicAppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = ClinicAppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return ClinicAppointment.objects.all()
        return ClinicAppointment.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        pet_id = self.request.data.get('pet_id')
        try:
            pet_to_book = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            raise serializers.ValidationError("Hewan peliharaan tidak ditemukan.")
        
        if pet_to_book.owner != self.request.user:
            raise PermissionDenied("You can only book appointments for your own pets.")
        
        serializer.save(user=self.request.user, pet=pet_to_book)

class GroomingBookingViewSet(viewsets.ModelViewSet):
    serializer_class = GroomingBookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return GroomingBooking.objects.all()
        return GroomingBooking.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        pet_id = self.request.data.get('pet_id')
        try:
            pet_to_book = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            raise serializers.ValidationError("Hewan peliharaan tidak ditemukan.")
        
        if pet_to_book.owner != self.request.user:
            raise PermissionDenied("You can only book grooming for your own pets.")
        
        serializer.save(user=self.request.user, pet=pet_to_book)