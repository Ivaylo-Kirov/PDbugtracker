from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User) #when User is saved, it triggers a post_save signal, which we "listen to" here
def create_profile(sender, instance, created, **kwargs): # kwargs just accepts any additional arguments
    if created:
        Profile.objects.create(user=instance) #instance here is the instance of the User class that initiated the signal

@receiver(post_save, sender=User) # when User is saved, but it was an existing user, also save its profile
def save_profile(sender, instance, **kwargs): 
    instance.profile.save()