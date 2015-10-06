# encoding: utf-8
import json

from form_data.models import FormData


def test_convert_to_dict(sample_dict):
    data = json.dumps(sample_dict)
    converted_data = FormData.convert_to_dict(data)
    assert type(converted_data) == dict
    data = {k: json.dumps(v) for k, v in sample_dict.items()}
    converted_data = FormData.convert_to_dict(data)
    assert type(converted_data) == dict


def test_convert_values_to_string(sample_dict):
    converted_data = FormData.convert_values_to_string(sample_dict)
    assert all(type(v) == str for _, v in converted_data.items())


def test_setting(model, model_data):
    """Test for correct behavior of signal receiver

    The test checks if rendered html is set in post_save signal
    receiver method.
    """
    assert model.html != model_data['form']['html']
