# encoding: utf-8
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import FormData


class FormDataSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.CharField()
    title = serializers.CharField()
    form_id = serializers.CharField()
    action = serializers.CharField()
    enctype = serializers.CharField()
    method = serializers.CharField()
    help_text = serializers.CharField()
    css_classes = serializers.CharField()
    elements = serializers.CharField()
    elements_css_classes = serializers.CharField()

    class Meta:
        fields = (
            'url',
            'author',
            'title',
            'form_id',
            'action',
            'enctype',
            'method',
            'help_text',
            'css_classes',
            'elements',
            'elements_css_classes',
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
            'elements_css_classes']
        return_data.update({key: form_data.get(key, None) for key in form_data_keys})
        return_data['elements'] = FormData.order_by_weight(form_data.get('elements', {}))
        form_id = form_data.get('id', None)
        if form_id:
            return_data['form_id'] = form_id
        return return_data

    def to_representation(self, obj):
        meta_attrs = ['date_created', 'date_updated', 'html']
        representation = {key: getattr(obj, key) for key in meta_attrs}
        representation['author'] = obj.author_id
        form_attrs = ['title', 'form_id', 'action', 'enctype', 'method', 'help_text',
            'css_classes', 'elements_css_classes']
        representation['form'] = {key: getattr(obj, key) for key in form_attrs}
        representation['form']['elements'] = FormData.order_by_weight(
            obj.convert_to_dict(getattr(obj, 'elements'))
        )
        request = self.context.get('request')
        representation['url'] = reverse('api-detail', kwargs={'pk': obj.id}, request=request)
        return representation
