# encoding: utf-8
import pytest

from api.forms import HopperForm


@pytest.mark.django_db
def test_form_creation(model_data):
    html = HopperForm(data=model_data).render_as_form()
    assert html.startswith('<form')
