from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Pet
from .serializers import PetSerializer

# Create your views here.
class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        if self.request.user.is_staff:
            return Pet.objects.all()
        return Pet.objects.filter(owner=self.request.user)
        
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

