# encoding: utf-8
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt import utils

from .serializers import UserSerializer


class CreateUserView(APIView):
    """
    API View that receives a POST with a user's username and password.
    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = UserSerializer

    def post(self, request, format=None):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data = serializer.data
            payload = utils.jwt_payload_handler(serializer.instance)
            token = utils.jwt_encode_handler(payload)
            response_data.update(dict(token=token))
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
