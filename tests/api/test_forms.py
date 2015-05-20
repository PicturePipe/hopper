# encoding: utf-8
from api.forms import HopperForm


def test_form_creation(model_data):
    html = HopperForm(data=model_data).render_as_form()
    assert html.startswith('<form')
