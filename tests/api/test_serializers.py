# encoding: utf-8
import pytest

from api.serializers import FormDataSerializer


@pytest.mark.parametrize("key", [
    ('author'),
    ('title'),
    ('action'),
    ('method'),
    ('enctype'),
    ('help_text'),
    ('css_classes'),
    ('elements_css_classes'),
])
def test_form_serializer(model, model_data, key):
    serializer = FormDataSerializer(model)
    assert serializer.data[key] == model_data[key]
