from django.contrib import admin
from .models import(
    LessonTeacher,
    LessonType,
    LessonDegree,
    Lesson,
    Banner
)


# Register your models here.
@admin.register(LessonTeacher)
class LessonTeacherModelAdmin(admin.ModelAdmin):
    fields = (
        'name',
    )


@admin.register(LessonType)
class LessonTypeModelAdmin(admin.ModelAdmin):
    fields = (
        'name',
    )


@admin.register(LessonDegree)
class LessonDegreeModelAdmin(admin.ModelAdmin):
    fields = (
        'name',
    )


@admin.register(Lesson)
class LessonModelAdmin(admin.ModelAdmin):
    fields = (
        'mosque',
        'type',
        'degree_type',
        'periodicity',
        'teacher',
        'gender',
        'start_time',
        'end_time',
        'week_day',
        'start_date'
    )


@admin.register(Banner)
class BannerModelAdmin(admin.ModelAdmin):
    fields = (
        'image',
        'lesson',
        'featured',
    )