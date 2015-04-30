# encoding: utf-8
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import FormData


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
    elements = serializers.DictField(required=False)
    html = serializers.CharField(required=False)
    id = serializers.IntegerField(required=False)
    method = serializers.CharField(required=False)
    action = serializers.CharField(required=False)
    enctype = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    help_text = serializers.CharField(required=False)
    css_classes = serializers.CharField(required=False)
    elements_css_classes = serializers.CharField(required=False)

    class Meta:
        fields = (
            'id',
            'author',
            'elements',
            'html',
            'form',
            'title',
            'action',
            'enctype',
            'method',
            'help_text',
            'css_classes',
            'elements_css_classes',
        )
        model = FormData

    def create(self, validated_data):
        form_data = validated_data.pop('form')
        form_data['elements'] = self.initial_data['form'].pop('elements')
        validated_data.update(form_data)
        return FormData.objects.create(**validated_data)
