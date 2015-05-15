# encoding: utf-8
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import FormData


class FormDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = (
            'url',
        )
        model = FormData

    def create(self, validated_data):
        return FormData.objects.create(**validated_data)

    def to_internal_value(self, data):
        return_data = {}
        author_id = data.pop('author', None)
        author = User.objects.get(id=author_id)
        if author:
            return_data['author'] = author
        form_data = data.pop('form', None)
        form_data_keys = ['method', 'action', 'enctype', 'title', 'help_text', 'css_classes',
            'elements_css_classes', 'elements']
        return_data.update({key: form_data.get(key, None) for key in form_data_keys})
        form_id = form_data.get('id', None)
        if form_id:
            return_data['form_id'] = form_id
        return return_data

    def to_representation(self, obj):
        object_attrs = ['title', 'date_created', 'date_updated', 'form_id', 'action', 'enctype',
            'method', 'help_text', 'css_classes', 'elements_css_classes', 'html']
        representation = {key: getattr(obj, key) for key in object_attrs}
        representation['author'] = obj.author_id
        representation['elements'] = obj.convert_to_dict(getattr(obj, 'elements'))
        return representation
