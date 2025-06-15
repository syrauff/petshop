from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
# Jadikan password write_only agar tidak pernah dikirim kembali dalam response API
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        # Ini adalah langkah keamanan yang PALING PENTING.
        # Kita menggunakan create_user untuk membuat user dan MENG-HASH password.
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', '')
        )
        user.save()
        return user
