# encoding: utf-8
from .models import FormData

from django.contrib.auth.models import User

from rest_framework import serializers


class AuthorSerializer(serializers.IntegerField):
    def to_internal_value(self, data):
        return User.objects.get(id=data)

    def to_representation(self, value):
        return User.objects.get(username=value).id


class FormSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    method = serializers.CharField()
    action = serializers.CharField()
    enctype = serializers.CharField()
    title = serializers.CharField()
    help_text = serializers.CharField()
    css_classes = serializers.CharField()
    elements_css_classes = serializers.CharField()


class FormDataSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer()
    form = FormSerializer(required=False)

    class Meta:
        fields = (
            'author',
            'date_created',
            'date_updated',
            'html',
            'form',
        )
        model = FormData

    def create(self, validated_data):
        form_data = validated_data.pop('form')
        form_data['elements'] = self.initial_data['form'].pop('elements')
        validated_data.update(form_data)
        return FormData.objects.create(**validated_data)
