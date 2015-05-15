# encoding: utf-8
from rest_framework import viewsets

from .models import FormData
from .serializers import FormDataSerializer


class FormDataViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = FormDataSerializer
    queryset = FormData.objects.all()

    def get_serializer(self, *args, **kwargs):
        """
        Return serializer instance with injected context.
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
