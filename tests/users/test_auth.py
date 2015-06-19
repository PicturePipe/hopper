# encoding: utf-8
import json

import pytest
from django.core.urlresolvers import reverse


def test_obtain_token_for_existing_user(client, user, credentials):
    url = reverse('obtain_jwt')
    email, password = credentials
    data = {'email': email, 'password': password}
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert response.data.get('token')


def test_login_with_token(client, user, token):
    url = reverse('api-root')
    response = client.get(url, HTTP_AUTHORIZATION='JWT {0}'.format(token(user)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_user_with_wrong_token(client, user, token):
    url = reverse('create_user')
    data = {}
    response = client.post(url, data=json.dumps(data), content_type='application/json',
        HTTP_AUTHORIZATION='JWT {0}'.format('abc'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_create_user_bad_request(client, user, token):
    # It is not allowed to create master user via API
    url = reverse('create_user')
    data = {
        'is_master': True,
    }
    response = client.post(url, data=json.dumps(data), content_type='application/json',
        HTTP_AUTHORIZATION='JWT {0}'.format(token(user)))
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_user_with_master_token(client, master_user, token):
    url = reverse('create_user')
    data = {'email': 'user1@example.com', 'password': 'seCret_passw0rd',
        'master_token': token(master_user)}
    response = client.post(url, data=json.dumps(data), content_type='application/json',
        HTTP_AUTHORIZATION='JWT {0}'.format(token(master_user)))
    assert response.status_code == 201
