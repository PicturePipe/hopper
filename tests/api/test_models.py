# encoding: utf-8
import json

import pytest

from api.models import FormData


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


def test_ordering_by_weight_with_form(form):
    ordered_elements = FormData.order_by_weight(form['form']['elements'])
    assert len(ordered_elements) == len(form['form']['elements'])
    ordered_director = ordered_elements['director'].pop('elements')
    # each level has to be ordered
    weights = [element['weight'] for element in ordered_elements.values()]
    assert sorted(weights) == weights
    weights = [element['weight'] for element in ordered_director.values()]
    assert sorted(weights) == weights


@pytest.mark.parametrize("elements, ordered_elements", [
    ({}, {}),
    ({'a': {}, 'b': {'weight': 1}}, {'b': {'weight': 1}, 'a': {}}),
])
def test_ordering_by_weight_edge_cases(elements, ordered_elements):
    assert FormData.order_by_weight(elements) == ordered_elements
