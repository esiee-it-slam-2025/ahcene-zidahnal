# mainapp/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import login
from ..serializers import RegisterSerializer, LoginSerializer, LogoutSerializer
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.urls import reverse_lazy

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({
                'message': 'Connexion réussie',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        print("ahcene")
        serializer = LogoutSerializer(data={}, context={'request': request})
        print("serializer is ok")
        serializer.is_valid()
        result = serializer.save()
        print("jam result", result)
        return Response(result, status=status.HTTP_200_OK)

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save() # Va automatiquement call les différentes méthodes de mon serializer 
            return Response({
                "user": serializer.data,
                "message": "Utilisateur créé avec succès"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
