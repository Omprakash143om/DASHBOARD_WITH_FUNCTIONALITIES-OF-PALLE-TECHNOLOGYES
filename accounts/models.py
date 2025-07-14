from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('sales', 'Sales'),
    )
    role= models.CharField(max_length=50, choices=ROLE_CHOICES, default='sales')
    
    
    
class Student(models.Model):
    added_by=models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    skills = models.CharField(max_length=255)  # Store comma-separated skills
    state = models.CharField(max_length=100)
    
def __str__(self):
    return self.name
