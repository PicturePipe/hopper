# encoding: utf-8
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework.reverse import reverse

from hopper.apps.form_data.models import FormData


class FormDataSerializer(serializers.HyperlinkedModelSerializer):
    AUTHOR_NOT_FOUND = _("You haven't send an author.")
    USER_NOT_FOUND = _("No author with this id found.")

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
        else:
            try:
                data['author']
            except KeyError:
                raise serializers.ValidationError(self.AUTHOR_NOT_FOUND)
            try:
                return_data['author'] = get_user_model().objects.get(pk=data['author'])
            except ObjectDoesNotExist:
                raise serializers.ValidationError(self.USER_NOT_FOUND)

        form_data = data.pop('form', None)
        form_data_keys = ['method', 'action', 'enctype', 'title', 'help_text', 'css_classes',
            'elements_css_classes', 'elements']
        return_data.update({key: form_data.get(key, None) for key in form_data_keys})
        return_data['form_id'] = form_data.get('id', "")
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
