# encoding: utf-8
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework_jwt import utils

from .models import HopperUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = HopperUser
        fields = ('username', 'password')

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        user = HopperUser.objects.create(**validated_data)
        return user

    def validate(self, attrs):
        is_master = self.data.pop('is_master', None)
        if is_master:
            raise ValidationError('Unknown attribute: is_master')
        else:
            master_token = self.data.pop('master_token', None)
            if not master_token:
                raise ValidationError('master_token not found')
            User = utils.get_user_model()
            master_user = User.objects.get(password=master_token)
            if master_user:
                attrs['site'] = master_user.site
            else:
                raise ValidationError('No user for this sent token.')
        return attrs
