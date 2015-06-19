# encoding: utf-8
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework_jwt import utils

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        user = User.objects.create(**validated_data)
        return user

    def validate(self, attrs):
        is_master = self.initial_data.pop('is_master', None)
        if is_master:
            raise ValidationError('Unknown attribute: is_master')
        else:
            master_token = self.initial_data.pop('master_token', None)
            if not master_token:
                raise ValidationError('master_token not found')
            master_infos = utils.jwt_decode_handler(master_token)
            master_user = User.objects.get(pk=master_infos.get('user_id'))
            if master_user:
                attrs['site'] = master_user.site
            else:
                raise ValidationError('No user for this sent token.')
        return attrs
