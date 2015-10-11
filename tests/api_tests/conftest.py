# encoding: utf-8
import json

import pytest
from pytest_factoryboy import LazyFixture, register

from . import factories


@pytest.fixture
def elements(fixture):
    return json.loads(fixture('simple_form.json'))['form']['elements']


@pytest.fixture
def password(scope='module'):
    """Return the default test password."""
    return "test"


@pytest.fixture
def login(client, user, password):
    """Return the User instance after logging the user in."""
    assert client.login(username=user.username, password=password)
    return user


register(factories.FormDataFactory, 'form', elements=LazyFixture('elements'))
register(factories.FormDataFactory, 'form_with_user', author=LazyFixture('user'))
