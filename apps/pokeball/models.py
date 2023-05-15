from django.db import models


apricorns = ['white', 'pink', 'black', 'red', 'yellow', 'blue', 'green']


class PokeballModel(models.Model):
    class Meta:
        verbose_name = 'Покебол'
        verbose_name_plural = 'Покеболы'

    name = models.CharField(max_length=100)
    craft_recipie = models.CharField(max_length=100)
    crafted_count = models.PositiveSmallIntegerField()
    wanted_count = models.PositiveSmallIntegerField()
