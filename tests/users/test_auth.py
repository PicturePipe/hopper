# encoding: utf-8
import json

from django.core.urlresolvers import reverse


def test_obtain_token_for_existing_user(client, user, credentials):
    url = reverse('obtain_jwt')
    username, password = credentials
    data = {'username': username, 'password': password}
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert response.data.get('token')
