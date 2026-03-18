from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio_content = models.TextField(
        validators = [
            MinLengthValidator(256, '')
            ]
        )
    
    def __str__(self):
        return self.name