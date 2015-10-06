# encoding: utf-8
from django.views import generic
from rest_framework import viewsets

from . import models
from .serializers import FormDataSerializer


class FormDataViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing form instances.
    """
    serializer_class = FormDataSerializer
    queryset = models.FormData.objects.all()

    def get_serializer(self, *args, **kwargs):
        """
        Return serializer instance with injected context.
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class FormDataListView(generic.ListView):
    """View that shows all from of the current user."""
    model = models.FormData
    ordering = 'title'

    def get_queryset(self):
        return models.FormData.objects.user_related(self.request.user.id)
