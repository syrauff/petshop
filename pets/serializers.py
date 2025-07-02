from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    
    owner_username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Pet
        fields = ['id', 'name', 'species', 'breed', 'age', 'weight', 'notes', 'owner', 'owner_username']
        read_only_fields = ['owner']
