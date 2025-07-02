from django.contrib.auth.models import User
from .serializers import RegisterSerializer, ProfileSerializer, UserManagementSerializer
from .permissions import IsSuperuser
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    # Izinkan semua pengguna (bahkan yang belum login) untuk mengakses view ini
    permission_classes = []  

class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Mengembalikan user yang sedang login
        return self.request.user

class UserManagementViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserManagementSerializer
    permission_classes = [IsSuperuser]

