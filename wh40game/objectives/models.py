from django.db import models


class RulesVersion(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название пака правил')
    #  rules_type = models.CharField()
    actual_version = models.BooleanField(default=True, verbose_name='Актуальная ли это версия')
    short_name = models.CharField(max_length=5, verbose_name='Короткое название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Набор правил'
        verbose_name_plural = 'Наборы правил'


class ObjectiveType(models.Model):
    #  VERSION_CHOICES = [('gt20' , 'Grand Tournament 2021'), ('ow', 'Open War'), ('old', 'Старые миссии')]
    name = models.CharField(max_length=30, verbose_name='Название типа вторичной миссии')
    version = models.CharField(max_length=20, verbose_name='Версия вторичек')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип вторичной миссии'
        verbose_name_plural = 'Типы вторичной миссии'

