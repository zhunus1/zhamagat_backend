from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = "Название",
    )

    created = models.DateTimeField(
        verbose_name = "Создано",
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = "Обновлено",
        auto_now = True,
    )

    def __str__(self):
        return "%s" % self.name
    
    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class City(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = "Название",
    )

    region = models.ForeignKey(
        Region, 
        on_delete = models.CASCADE,
        verbose_name = "Регион",
        related_name = 'cities'
    )
    
    created = models.DateTimeField(
        verbose_name = "Создано",
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = "Обновлено",
        auto_now = True,
    )

    def __str__(self):
        return "%s" % self.name
    
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Mosque(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = "Название",
    )

    city = models.ForeignKey(
        City, 
        on_delete = models.CASCADE,
        verbose_name = "Город",
        related_name = 'mosques'
    )
    
    image = models.FileField(
        upload_to = 'mosques/',
        verbose_name = "Изображение",
    )

    created = models.DateTimeField(
        verbose_name = "Создано",
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = "Обновлено",
        auto_now = True,
    )

    def __str__(self):
        return "%s" % self.name
    
    class Meta:
        verbose_name = "Мечеть"
        verbose_name_plural = "Мечети"