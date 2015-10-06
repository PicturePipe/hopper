# encoding: utf-8
import pytest
from pytest_factoryboy import LazyFixture

from api import models


@pytest.mark.django_db
@pytest.mark.parametrize(('form__author', 'count'), [
    (LazyFixture('user'), 1), (LazyFixture('alternative_user'), 0),
])
def test_queryset_user_related(form, user, count):
    assert models.FormData.objects.user_related(user.id).count() == count
