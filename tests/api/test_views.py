# encoding: utf-8
import httpretty
import pytest
from django.core.urlresolvers import reverse


@pytest.mark.httpretty
def test_get_api_root(client, user, token):
    url = reverse('api-root')
    httpretty.register_uri(httpretty.GET, url, content_type='application/json')
    get_response = client.get(url, HTTP_AUTHORIZATION='JWT {0}'.format(token(user)))
    assert get_response.status_code == 200


@pytest.mark.httpretty
@pytest.mark.django_db
def test_list_view_get(client, fixture, user, token):
    url = reverse('api-list')
    httpretty.register_uri(httpretty.GET, url,
        body=fixture('base_form.json'), content_type='application/json')
    response = client.get(url, HTTP_AUTHORIZATION='JWT {0}'.format(token(user)))
    assert response.status_code == 200


@pytest.mark.httpretty
def test_list_view_post(client, form_data, user, token):
    url = reverse('api-list')
    httpretty.register_uri(httpretty.POST, url, body=form_data,
        content_type='application/json')
    response = client.post(url, data=form_data, content_type='application/json',
        HTTP_AUTHORIZATION='JWT {0}'.format(token(user)))
    assert response.status_code == 201


@pytest.mark.httpretty
@pytest.mark.django_db
def test_list_view_detail(client, fixture, model, user, token):
    url = reverse('api-detail', kwargs={'pk': model.id})
    httpretty.register_uri(httpretty.GET, url,
        body=fixture('base_form.json'), content_type='application/json')
    response = client.get(url, HTTP_AUTHORIZATION='JWT {0}'.format(token(user)))
    assert response.status_code == 200
    assert response.data['url'].startswith('http://')
