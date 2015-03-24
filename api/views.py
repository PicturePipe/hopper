from rest_framework import viewsets

from .models import FormData
from .serializers import FormDataSerializer


class FormDataViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = FormDataSerializer
    queryset = FormData.objects.all()
