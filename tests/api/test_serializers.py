# encoding: utf-8
from api.serializers import FormDataSerializer


def test_form_serializer(model):
    keys = ('title', 'action', 'method', 'enctype', 'help_text', 'css_classes',
        'elements_css_classes',)
    serializer = FormDataSerializer(model)
    for key in keys:
        assert serializer.data[key] == getattr(model, key)
    assert serializer.data['author'] == model.author.pk
