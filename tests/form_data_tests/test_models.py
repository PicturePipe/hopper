# encoding: utf-8
import pytest


@pytest.mark.django_db
def test_setting(model, model_data):
    """Test for correct behavior of signal receiver

    The test checks if rendered html is set in post_save signal
    receiver method.
    """
    assert model.html != model_data['form']['html']
