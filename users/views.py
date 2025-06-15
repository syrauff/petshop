from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RegisterSerializer


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    # Izinkan semua pengguna (bahkan yang belum login) untuk mengakses view ini
    permission_classes = []  