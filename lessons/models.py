from django.db import models
from django.core.validators import FileExtensionValidator

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
    

class LessonDegree(models.Model):
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
        verbose_name = "Уровень урока"
        verbose_name_plural = "Уровни уроков"


class Lesson(models.Model):
    CHOICES = (
        ('MALE', 'Мужчины'),
        ('FEMALE', 'Женщины'),
    )

    WEEK_DAYS = (
        ('MN', 'Понедельник'),
        ('TU', 'Вторник'),
        ('WD', 'Среда'),
        ('TH', 'Четверг'),
        ('FR', 'Пятница'),
        ('ST', 'Суббота'),
        ('SN', 'Воскресенье'),
    )

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

    degree_type = models.ForeignKey(
        LessonDegree, 
        on_delete = models.CASCADE,
        verbose_name = "Уровень урока",
        related_name = 'lessons',
        blank=True, 
        null=True
    )

    periodicity = models.BooleanField(
        default = False,
        verbose_name = "Еженедельно",
    )

    teacher = models.ForeignKey(
        LessonTeacher, 
        on_delete = models.CASCADE,
        verbose_name = "Учитель",
        related_name = 'lessons'
    )

    gender = models.CharField(
        max_length = 7, 
        choices = CHOICES,
        verbose_name = "Для кого",
    )

    start_time = models.TimeField(
        verbose_name = "Время начала",
    )

    end_time = models.TimeField(
        verbose_name = "Время конца",
    )

    week_day = models.CharField(
        max_length = 7, 
        choices = WEEK_DAYS,
        verbose_name = "День недели",
    )

    start_date = models.DateField(
        verbose_name = "Старт курса",
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
        validators = [
            FileExtensionValidator(
                allowed_extensions=["png", "jpg", "jpeg"]
            )
        ],
    )

    lesson = models.ForeignKey(
        Lesson, 
        on_delete = models.CASCADE,
        verbose_name = "Урок",
        related_name = 'banners'
    )
    
    featured = models.BooleanField(
        default = False,
        verbose_name = "Отображать на главной",
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
