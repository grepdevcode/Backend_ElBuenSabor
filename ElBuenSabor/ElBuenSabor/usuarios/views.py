from django.shortcuts import render
#from django.contrib.auth.models import User, Group
from .models import Cliente
from rest_framework import viewsets
from .serializers import ClienteSerializer
from rest_framework import generics


# class UserViewSet(viewsets.ModelViewSet):
class UserViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class UserViewSetDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
