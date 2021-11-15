from django.db import models
from ..objectives.models import *


class Race(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название расы')
    short_name = models.CharField(max_length=5, verbose_name='Сокращение')


class Game(models.Model):
    #  rule_pack = models.ForeignKey(RulesVersion, on_delete=models.CASCADE, verbose_name='Используемые пр'
    player_1_race = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name='Раса первого игрока')
    player_1_name = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name='Ник первого игрока')
    player_2_race = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name='Раса второго игрока')
    player_2_name = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name='Ник второго игрока')
