# encoding: utf-8

import factory

from form_data import models
from tests import factories as global_factories


class FormDataFactory(factory.DjangoModelFactory):
    author = factory.SubFactory(global_factories.UserFactory)
    title = 'form title'
    action = '/action/create'
    method = 'POST'
    enctype = 'multipart/form-data'
    html = '<form></form>'
    help_text = 'help, HELP!!'
    css_classes = 'form inline'
    elements_css_classes = 'form-control'
    elements = ''

    class Meta:
        model = models.FormData
