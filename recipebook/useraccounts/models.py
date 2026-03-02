from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio_content = models.TextField(
        validators = [
            MinLengthValidator(256, '')
            ]
        )