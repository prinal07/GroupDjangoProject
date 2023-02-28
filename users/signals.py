from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User as django_user

from .models import Profile, Account


@receiver(post_save, sender=django_user)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=django_user)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

