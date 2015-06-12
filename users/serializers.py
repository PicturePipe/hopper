# encoding: utf-8
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from rest_framework import serializers
from rest_framework_jwt import utils
from rest_framework_jwt.serializers import JSONWebTokenSerializer


class UserJSONWebTokenSerializer(JSONWebTokenSerializer):

    def __init__(self, *args, **kwargs):
        """
        Dynamically add the USERNAME_FIELD to self.fields.
        """
        self.master_token = kwargs['data'].pop('master_token', None)
        super(UserJSONWebTokenSerializer, self).__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField()

    def validate(self, attrs):
        # username, email? not pwd?
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }
        if self.master_token:
            User = utils.get_user_model()
            user = User.objects.create(**credentials)
            user.master_token = self.master_token
            user.save()
            return reverse('rest_framework_jwt.views.obtain_jwt_token')#, kwargs=attrs)
        else:
            raise ValidationError('master_token is missing')
