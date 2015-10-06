# encoding: utf-8
import pytest

from django.core.urlresolvers import reverse


@pytest.mark.django_db
def test_form_data_create_login_required(client):
    response = client.get(reverse('form_data_create'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_form_data_create_login_post(credentials, user, client):
    username, password = credentials
    from form_data.models import FormData
    assert client.login(username=username, password=password)
    assert not FormData.objects.count()
    response = client.post(reverse('form_data_create'), data={'title': 'Test'})
    assert response.status_code == 302
    assert FormData.objects.count()
