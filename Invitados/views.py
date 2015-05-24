from django.shortcuts import render
from Invitados.models import Invitado
from rest_framework import viewsets
from Invitados.serializers import InvitadoSerializer

class InvitadoViewSet(viewsets.ModelViewSet):
     """
    API endpoint that allows users to be viewed or edited.
    """
     queryset = Invitado.objects.all()
     serializer_class = InvitadoSerializer