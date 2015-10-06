# encoding: utf-8
import json

import pytest
from pytest_factoryboy import LazyFixture, register

from tests import factories as global_factories

from . import factories

register(factories.FormDataFactory, 'form', elements=LazyFixture('elements'))
register(global_factories.UserFactory, 'user')
register(global_factories.UserFactory, 'alternative_user')
register(factories.FormDataFactory, 'form_with_user', author=LazyFixture('user'))


@pytest.fixture
def elements(fixture):
    return json.loads(fixture('simple_form.json'))['form']['elements']
