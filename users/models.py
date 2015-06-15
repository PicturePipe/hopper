# encoding: utf-8
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.sites.models import Site
from django.db import models


class HopperUser(AbstractBaseUser):
    username = models.CharField(max_length=200)
    is_master = models.BooleanField(default=False)
    site = models.ForeignKey(Site)

    class Meta:
        unique_together = (("username", "site"),)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
