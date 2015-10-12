# encoding: utf-8
import json

import pytest
from pytest_factoryboy import LazyFixture, register

from . import factories


@pytest.fixture
def elements(fixture):
    return json.loads(fixture('simple_form.json'))['form']['elements']


register(factories.FormDataFactory, 'form', elements=LazyFixture('elements'))
register(factories.FormDataFactory, 'form_with_user', author=LazyFixture('user'))
