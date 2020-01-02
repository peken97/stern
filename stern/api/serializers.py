from rest_framework import serializers
from api.models import Environment, LegoPiece, Model

class EnvironmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)