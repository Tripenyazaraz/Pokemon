from rest_framework import serializers

from apps.pokeball import models


class PokeballSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PokeballModel
        fields = "__all__"
