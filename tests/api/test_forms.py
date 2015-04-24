# encoding: utf-8
from api.forms import HopperForm


def test_form_creation(user, form_data_model):
    html = HopperForm(model=form_data_model).render_as_form()
    assert html.startswith('<form')
