from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegistrationSerializer
from user_app import models


@api_view(['POST'])
def logout_view(request):
    
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
        


@api_view(['POST'])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
    
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'registration successful!'
            data['username'] = account.username
            data['email'] = account.email
            
            
            ###### for token authentication ##########
            token = Token.objects.get(user=account).key
            data['token'] = token
            
            
            ###### for JWT authentication ########
            # token = RefreshToken.for_user(account)
            # data['token'] = {
            #         'refresh': str(token),
            #         'access': str(token.access_token),
            # }
            
        else:
            data['error'] = serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)