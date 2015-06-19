# encoding: utf-8
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.sites.models import Site
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class HopperUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_master = models.BooleanField(default=False)
    site = models.ForeignKey(Site)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['site']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        unique_together = (('email', 'site'),)
