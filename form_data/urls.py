from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'create/$', views.FormDataCreateView.as_view(), name='form_data_create')
)
