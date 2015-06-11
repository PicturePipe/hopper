# encoding: utf-8
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers

from api.views import FormDataViewSet
from authentication.views import ObtainUserJSONWebToken

router = routers.DefaultRouter()
router.register(r'api', FormDataViewSet, base_name='api')

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/$', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^user-token-auth/', ObtainUserJSONWebToken.as_view(),
        name='obtain_user_jwt_token'),
    url(r'^', include(router.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
