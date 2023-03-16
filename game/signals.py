from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Challenge
from users.models import Account, ChallengeTracker

@receiver(post_save, sender=Challenge) 
def my_action(sender, instance, created, **kwargs):
    if created:
        accounts = Account.objects.all()
        for acc in accounts:
            ChallengeTracker.objects.create(
                account=acc,
                challenge=instance,
                completed=False
            )

        print(f"A new Challenge object was added with id {instance.challengeId}")

post_save.connect(my_action, sender=Challenge)
