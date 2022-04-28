from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.shortcuts import render
# from idna import unicode
from .models import User
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('password1',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']
        

class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def login_view(request, format=None):
    content = {
        'user': str(request.user),
        'auth': str(request.auth)
    }
    return Response(content)


