__author__ = 'jmmartinez'
from Invitados.models import Invitado
from rest_framework import serializers

class InvitadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invitado
        fields = ('telefono', 'nombre', 'activo')