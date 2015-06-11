# encoding: utf-8
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework import serializers
from rest_framework_jwt import utils
from django.core.urlresolvers import reverse


class UserJSONWebTokenSerializer(JSONWebTokenSerializer):

    def __init__(self, *args, **kwargs):
        """
        Dynamically add the USERNAME_FIELD to self.fields.
        """
        super(UserJSONWebTokenSerializer, self).__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField()

    def validate(self, attrs):
        User = utils.get_user_model()
        # username, email? not pwd?
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }
        user = User.objects.create(**credentials)
        user.master_token = attrs.pop('master_token', None)
        user.save()
        return reverse('obtain_jwt_token', kwargs=attrs)
