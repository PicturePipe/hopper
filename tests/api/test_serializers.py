# encoding: utf-8
from api.serializers import FormDataSerializer
from api.models import FormData


def test_form_serializer(model):
    keys = ('title', 'action', 'method', 'enctype', 'help_text', 'css_classes',
        'elements_css_classes',)
    serializer = FormDataSerializer(model)
    for key in keys:
        assert serializer.data[key] == getattr(model, key)
    assert serializer.data['author'] == model.author.pk


def test_serializer_with_minimal_model(user):
    model = FormData.objects.create(**{'author': user})
    serializer = FormDataSerializer(model)
    assert serializer.data['author'] == user.pk
