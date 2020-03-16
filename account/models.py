import os
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Account(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=18)
    room = models.CharField(max_length=8)
    dob = models.DateField(default=timezone.datetime.now())
    active = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='images/', default=os.path.join(settings.STATIC_ROOT, 'avatar.png'))
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.account.save()