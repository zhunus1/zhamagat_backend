from django.db import models

# Create your models here.
class LessonTeacher(models.Model):
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
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"


class LessonType(models.Model):
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
        verbose_name = "Тип урока"
        verbose_name_plural = "Типы уроков"


class Lesson(models.Model):
    mosque = models.ForeignKey(
        'mosques.Mosque', 
        on_delete = models.CASCADE,
        verbose_name = "Мечеть",
        related_name = 'lessons'
    )

    type = models.ForeignKey(
        LessonType, 
        on_delete = models.CASCADE,
        verbose_name = "Тип урока",
        related_name = 'lessons'
    )

    teacher = models.ForeignKey(
        LessonTeacher, 
        on_delete = models.CASCADE,
        verbose_name = "Учитель",
        related_name = 'lessons'
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
        return "%s" % self.pk
    
    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Banner(models.Model):
    image = models.FileField(
        upload_to = 'banners/',
        verbose_name = "Изображение",
    )

    lesson = models.ForeignKey(
        Lesson, 
        on_delete = models.CASCADE,
        verbose_name = "Урок",
        related_name = 'banners'
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
        return "%s" % self.pk
    
    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
