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

    def save(self, *args, **kwargs):
        if not self.short_name:
            self.short_name = self.name[:5]
            return super(RulesVersion, self).save(*args, **kwargs)
        else:
            return super(RulesVersion, self).save(*args, **kwargs)


class ObjectiveType(models.Model):
    #  VERSION_CHOICES = [('gt20' , 'Grand Tournament 2021'), ('ow', 'Open War'), ('old', 'Старые миссии')]
    OBJECTIVE_TYPES = [('prim', 'Primary objective from mission'), ('sec', 'Secondary objective mission')]
    name = models.CharField(max_length=30, verbose_name='Название типа вторичной миссии')
    rule_source = models.ForeignKey(RulesVersion, verbose_name='Откуда правила', on_delete=models.CASCADE)
    #  version = models.CharField(max_length=20, verbose_name='')
    obj_type = models.CharField(choices=OBJECTIVE_TYPES, default='sec', verbose_name='Тип класса обжективов', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип вторичной миссии'
        verbose_name_plural = 'Типы вторичных миссий'


class SecondaryObjective(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название миссии')
    rule_source = models.ForeignKey(RulesVersion, on_delete=models.CASCADE, verbose_name='Откуда правила')
    objective_type = models.ForeignKey(ObjectiveType, on_delete=models.CASCADE, verbose_name='Тип миссии')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(SecondaryObjective, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Вторичная миссия'
        verbose_name_plural = 'Вторичные миссии'
