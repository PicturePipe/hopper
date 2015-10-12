# encoding: utf-8
import pytest

from api.serializers import FormDataSerializer
from form_data.models import FormData


@pytest.mark.django_db
def test_form_serializer(model):
    keys = ('title', 'action', 'method', 'enctype', 'help_text', 'css_classes',
        'elements_css_classes',)
    serializer = FormDataSerializer(model)
    for key in keys:
        assert serializer.data['form'][key] == getattr(model, key)
    assert serializer.data['author'] == model.author.pk


@pytest.mark.django_db
def test_serializer_with_minimal_model(user):
    model = FormData.objects.create(**{'author': user})
    serializer = FormDataSerializer(model)
    assert serializer.data['author'] == user.pk
