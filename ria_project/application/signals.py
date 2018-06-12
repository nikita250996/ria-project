# coding: utf-8
from django.urls import reverse
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, EmployeeInfo, IntellectualProperty, Notification, NOTIFICATION_TYPE_CHOICES


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Create a matching profile whenever a user object is created."""
    if created:
        profile, new = EmployeeInfo.objects.get_or_create(user=instance)


@receiver(post_save, sender=IntellectualProperty)
def on_create_intellectual_property(sender, instance, created, **kwargs):
    if created:
        notification = Notification(
            time=now(), type=NOTIFICATION_TYPE_CHOICES[0],
            description="На площадке №{0} добавлена ""<a href='{1}'>новая заявка</a>".format(
                instance.ground.ground_code,
                reverse('request_intellectual_property_update', kwargs={'pk': instance.pk}))
        )
        notification.save()
