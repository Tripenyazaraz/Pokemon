from django.urls import path, include
from rest_framework import routers

from apps.pokeball import views

router = routers.DefaultRouter()

router.register(r'', views.PokeballViewSet, basename='pokeball_api')

urlpatterns = [
    path('', include(router.urls)),
]
