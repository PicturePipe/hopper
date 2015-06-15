# encoding: utf-8
import json
import pytest

from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site


def test_obtain_token_for_existing_user(client, user, credentials):
    url = reverse('obtain_jwt')
    username, password = credentials
    data = {'username': username, 'password': password}
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert response.data.get('token')


@pytest.mark.xfail
@pytest.mark.django_db
def test_create_master_user_bad_request(client):
    url = reverse('create_user')
    site = Site.objects.get_current()
    data = {
        'username': 'master1',
        'password': 'seCret_passw0rd',
        'is_master': True,
        'site': site.id,
    }
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400


@pytest.mark.xfail
@pytest.mark.django_db
def test_create_user_with_master_token(client, user, master_token):
    url = reverse('create_user')
    data = {'username': 'user1', 'password': 'seCret_passw0rd', 'master_token': master_token(user)}
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
