from django.db.models.signals import post_save #get post_save signals
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# @receiver(post_save, sender = User)
def create_profile(sender , instance , created , **kwargs):
    if created :
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)

# @receiver(post_save, sender = User)
def save_profile(sender , instance , **kwargs):
    instance.profile.save()

post_save.connect(create_profile, sender=User)