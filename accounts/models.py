from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')  # related_name 추가
    user_permissions = models.ManyToManyField('auth.Permission',
                                              related_name='custom_user_permissions')  # related_name 추가