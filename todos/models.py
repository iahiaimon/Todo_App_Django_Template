from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(unique=True , blank=False , null=False)
    email = models.EmailField(unique=True, blank=False , null=False)
    password = models.CharField(blank=False , null=False)
    confirm_password = models.CharField(blank=False , null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email} -- {self.username}"
    


class Todo(models.Model):
    title = models.CharField(blank=False , null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
