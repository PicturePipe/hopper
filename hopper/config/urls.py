# encoding: utf-8
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
from rest_framework_jwt.views import ObtainJSONWebToken

from api.views import FormDataViewSet

router = routers.DefaultRouter()
router.register(r'api', FormDataViewSet, base_name='api')

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/$', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^token-auth/', ObtainJSONWebToken.as_view(), name='obtain_jwt'),
    url(r'^users', include('users.urls')),
    url(r'^', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
