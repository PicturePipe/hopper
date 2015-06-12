# encoding: utf-8
from rest_framework_jwt.views import ObtainJSONWebToken
from .serializers import UserJSONWebTokenSerializer


class ObtainUserJSONWebToken(ObtainJSONWebToken):
    """
    API View that receives a POST with a user's username and password.
    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = UserJSONWebTokenSerializer
