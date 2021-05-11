from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView 
from .serializers import CustomUserSerializer
from rest_framework import permissions,status
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer
from rest_framework.views import APIView

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


class HelloWorldView(APIView):

    def get(self, request):
        return Response(data={"hello":"world"}, status=status.HTTP_200_OK)