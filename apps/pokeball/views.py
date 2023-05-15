from rest_framework.viewsets import ModelViewSet

from apps.pokeball import models, serializers


class PokeballViewSet(ModelViewSet):
    model = models.PokeballModel
    queryset = models.PokeballModel.objects.all()
    serializer_class = serializers.PokeballSerializer
