from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView 
from .serializers import CustomUserSerializer, UserProfileSerializer
from rest_framework import permissions,status
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer
from rest_framework.views import APIView
from .models import UserProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class ObtainTokenPairWithColorView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class CreateCustomUser(APIView):
    permission_classes=(permissions.AllowAny ,)

    def post(self,request ,format='json'):
        serializer = CustomUserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json_obj = serializer.data
                return Response(json_obj, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated, )


class BlacklistTokenUpdateView(APIView):
    permission_classes=(permissions.AllowAny ,)
    
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class HelloWorldView(APIView):

    def get(self, request):
        return Response(data={"hello":"world"}, status=status.HTTP_200_OK)


