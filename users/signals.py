#a signal get fire when a post is saved
from django.db.models.signals import post_save

#get a post save signal when user create, so import user
#user is a sender here
from django.contrib.auth.models import User

#a function of the signal that perform some tasks
from django.dispatch import receiver

#need to create profile in our function,
from .models import Profile

#run every a user is created
#when user is save, it send a signal to receiver
#receiver is create_profile()
#**kwargs allow it to recieve any additional keywords
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()