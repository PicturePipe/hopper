# encoding: utf-8
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse

from form_data.models import FormData


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
        if self.instance:
            return_data['author'] = self.instance.author
        elif 'author' in data:
            return_data['author'] = get_user_model().objects.get(pk=data['author'])
        form_data = data.pop('form', None)
        form_data_keys = ['method', 'action', 'enctype', 'title', 'help_text', 'css_classes',
            'elements_css_classes', 'elements']
        return_data.update({key: form_data.get(key, None) for key in form_data_keys})
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
        representation['form']['elements'] = getattr(obj, 'elements')
        request = self.context.get('request')
        representation['url'] = reverse('api-detail', kwargs={'pk': obj.id}, request=request)
        return representation
