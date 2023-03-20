from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User as django_user

from .models import Profile, Account, Challenge, ChallengeTracker


@receiver(post_save, sender=django_user)
def create_profile(sender, instance, created, **kwargs):
    """
    Creates a profile picture based on the Django user
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=django_user)
def save_profile(sender, instance, **kwargs):
    """
    Ensures profile is saved in database
    """
    instance.profile.save()


@receiver(post_save, sender=Challenge)
def create_challengestatus(sender, instance, created, **kwargs):
    """
    Creates a challenge under account model

    """
    if not created:
        # Challenge object has been updated
        for status in ChallengeTracker.objects.filter(challenge=instance):
            # Create a copy of the ChallengeStatus object
            ChallengeTracker.objects.create(
                account=status.account,
                challenge=instance,
                completed=status.completed
            )


@receiver(post_save, sender=Account)
def create_account_challenges(sender, instance, created, **kwargs):
    """

    """
    if created:
        challenges = Challenge.objects.all()
        for challenge in challenges:
            ChallengeTracker.objects.create(
                account=instance,
                challenge=challenge,
                completed=False
            )
