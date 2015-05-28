# encoding: utf-8
import json
import os

import pytest

from api.models import FormData


@pytest.fixture
def credentials():
    return ('testuser', 'testpwd')


@pytest.fixture
def user(credentials, django_user_model, db):
    username, password = credentials
    return django_user_model.objects.create_user(username=username, password=password)


@pytest.fixture
def fixture():
    def load(name):
        fixture = os.path.join(os.path.dirname(__file__), 'fixtures', name)
        with open(fixture) as f:
            return f.read()
    return load


@pytest.fixture
def model_data(user, form):
    model_data = {
        'author': user.id,
        'form': {
            'title': 'my form',
            'action': '/action/create',
            'method': 'POST',
            'enctype': 'multipart/form-data',
            'html': '<form></form>',
            'help_text': 'help, HELP!!',
            'css_classes': 'form inline',
            'elements_css_classes': 'form-control',
            'elements': form['form']['elements'],
        }
    }
    return model_data


@pytest.fixture
def model(model_data, user):
    model_data['form']['author'] = user
    return FormData.objects.create(**model_data['form'])


@pytest.fixture
def form(fixture, user):
    form_data = json.loads(fixture('form.json'))
    return form_data


@pytest.fixture
def sample_dict():
    data = {
        '1': 'string',
        '2': [1, 2, 3, 4, 5],
        '3': {
            '1': 'string',
            '2': [1, 2, 3, 4, 5],
        }
    }
    return data
