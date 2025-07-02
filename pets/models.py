from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
    SPECIES_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('fish', 'Fish'),
        ('reptile', 'Reptile'),
        ('other', 'Other'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField(help_text="Age in years")
    weight = models.DecimalField(max_digits=5, decimal_places=2, help_text="Weight in kg")
    notes = models.TextField(blank=True, null=True, help_text="Additional notes about the pet")

    def __str__(self):
        return f"{self.name} ({self.species}) - Owner: {self.owner.username}"

    