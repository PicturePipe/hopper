# encoding: utf-8
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.sites.models import Site
from django.db import models


class HopperUser(AbstractBaseUser):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField('email address', blank=True)
    is_master = models.BooleanField(default=False)
    site = models.ForeignKey(Site)
    is_staff = models.BooleanField('staff status', default=False,
        help_text='Designates whether the user can log into this admin '
                    'site.')
    is_active = models.BooleanField('active', default=True,
        help_text='Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')

    objects = UserManager()

    class Meta:
        unique_together = (("username", "site"),)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
