from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User) #when User is saved, send post_save signal, which the function below will receive
def create_profile(sender, instance, created, **kwargs): # kwargs just accepts any additional arguments
    if created:
        Profile.objects.create(user=instance) #instance here is the instance of the User class that initiated this signal

@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs): 
    instance.profile.save()