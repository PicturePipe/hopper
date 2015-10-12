# encoding: utf-8
import pytest
from django.core.urlresolvers import reverse


@pytest.mark.django_db
def test_form_data_create_login_required(client):
    response = client.get(reverse('form_data_create'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_form_data_create_login_post(user, login, client):
    from form_data.models import FormData
    assert not FormData.objects.count()
    response = client.post(reverse('form_data_create'), data={'title': 'Test'})
    assert response.status_code == 302
    assert FormData.objects.count()


@pytest.mark.django_db
def test_form_data_update_ownership_required(form_with_other_user, user, login, client):
    assert form_with_other_user.author != user
    response = client.get(reverse('form_data_update', kwargs={'pk': form_with_other_user.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_form_data_update_ownership_create_token(model, user, login, client):
    from rest_framework.authtoken.models import Token
    assert model.author == user
    assert not Token.objects.count()
    client.get(reverse('form_data_update', kwargs={'pk': model.pk}))
    assert Token.objects.count()
    assert Token.objects.filter(user=user).count()


@pytest.mark.django_db
def test_list_view(client, login, form):
    url = reverse('form_data_list')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.context['formdata_list']) == 1
