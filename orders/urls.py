from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, ClinicAppointmentViewSet, GroomingBookingViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'clinic-appointments', ClinicAppointmentViewSet, basename='clinic-appointment')
router.register(r'grooming-bookings', GroomingBookingViewSet, basename='grooming-booking')

urlpatterns = [
    path('', include(router.urls)),
]
