from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(
        max_length=255,
        verbose_name="Номер телефона",
        null=True, blank=True
    )
    coins = models.CharField(
        max_length=255,
        verbose_name="Монеты",
        null=True, blank=True,
        default="0")

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

