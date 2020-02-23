from django.db.models.signals import post_save

# User sends the signal
from django.contrib.auth.models import User

# A receiver is a function that gets the signal and then performs some tasks
from django.dispatch import receiver

from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print(f'Created profile for {instance.username}!')

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    print(f'Saved {instance.username}\'s profile!')
