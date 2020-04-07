from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=100)

    
class Image(models.Model):
    url = models.TextField()

    
class Book(models.Model):
    title = models.TextField()
    price = models.FloatField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    image = models.OneToOneField(Image, on_delete=models.CASCADE)
    
    
@receiver(post_save, sender=CustomUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)