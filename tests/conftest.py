# encoding: utf-8
import json
import os

import pytest
from django.contrib.sites.models import Site
from rest_framework_jwt import utils

from api.models import FormData
from users.models import HopperUser


@pytest.fixture
def credentials():
    return ('testuser', 'testpwd')


@pytest.fixture
def user(credentials, db):
    username, password = credentials
    data = {
        'username': username,
        'site': Site.objects.get_current()
    }
    user = HopperUser.objects.create(**data)
    user.set_password(password)
    user.save()
    return user


@pytest.fixture
def master_user(user):
    user.is_master = True
    user.save()
    return user


@pytest.fixture
def fixture():
    def load(name):
        fixture = os.path.join(os.path.dirname(__file__), 'fixtures', name)
        with open(fixture) as f:
            return f.read()
    return load


@pytest.fixture
def model_data(user, fixture):
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
            'elements': json.loads(fixture('simple_form.json'))['form']['elements'],
        }
    }
    return model_data


@pytest.fixture
def model(model_data, user):
    model_data['form']['author'] = user
    return FormData.objects.create(**model_data['form'])


@pytest.fixture
def form_data(fixture, user):
    form_data = json.loads(fixture('simple_form.json'))
    form_data['author'] = user.id
    return json.dumps(form_data)


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


@pytest.fixture
def token():
    def get_token(user):
        payload = utils.jwt_payload_handler(user)
        return utils.jwt_encode_handler(payload)
    return get_token
