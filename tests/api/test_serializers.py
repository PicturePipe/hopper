# encoding: utf-8
from form_data.models import FormData
from api.serializers import FormDataSerializer


def test_form_serializer(model):
    keys = ('title', 'action', 'method', 'enctype', 'help_text', 'css_classes',
        'elements_css_classes',)
    serializer = FormDataSerializer(model)
    for key in keys:
        assert serializer.data['form'][key] == getattr(model, key)
    assert serializer.data['author'] == model.author.pk


def test_serializer_with_minimal_model(user):
    model = FormData.objects.create(**{'author': user})
    serializer = FormDataSerializer(model)
    assert serializer.data['author'] == user.pk
