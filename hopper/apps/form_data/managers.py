# encoding: utf-8
from django.db import models


class FormDataQuerySet(models.QuerySet):
    def user_related(self, user_id):
        """This QS returns all user related Forms."""
        return self.filter(author=user_id)


class FormDataManager(models.Manager):
    use_for_related_fields = True
