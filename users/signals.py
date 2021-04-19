from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile

#create_profile se va a correr cada vez que se guarde una instancia en el USER MODEL
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # created es asignado True cuando la instancia es creada
    if created:
        profile = Profile(user=instance)
        profile.save()

    


# las signals son un sistema de comunicacion entre aplicaciones