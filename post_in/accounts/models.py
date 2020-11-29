from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

class UserProfile(models.Model):
    email = models.EmailField(unique=True, blank=False, max_length=50)
    username = models.CharField(unique=True, blank=False, max_length=50)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'{self.username}'

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.username