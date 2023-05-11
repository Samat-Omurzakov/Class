from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from users.serializers import UserCreatSerializer, UserAuthorizeSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# Create your views here.

@api_view(['Post'])
def authorization_api_view(request):
    """ Validate data """
    serializer = UserAuthorizeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    """ Read data """
    # username = serializer.validated_data.get('username')
    # password = serializer.validated_data.get('password')
    """ Authenticate (search) User"""
    # user = authenticate(username=username, password=password)
    user = authenticate(**serializer.validated_data)
    if user:
        """ Authorize User"""
        # Token.objects.filter(user=user).delete()
        # token = Token.objects.create(user=user)
        token, craeted = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    """ Error om Unauthorizing """
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['Post'])
def registration_api_view(request):
    serializer = UserCreatSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.create_user(username=username, password=password)
    return Response(data={'user_id': user.id})
