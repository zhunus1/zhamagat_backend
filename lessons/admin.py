from django.contrib import admin
from .models import(
    LessonTeacher,
    LessonType,
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


@admin.register(Lesson)
class LessonModelAdmin(admin.ModelAdmin):
    fields = (
        'mosque',
        'type',
        'teacher',
        'gender',
        'start_time',
        'end_time',
        'date'
    )


@admin.register(Banner)
class BannerModelAdmin(admin.ModelAdmin):
    fields = (
        'image',
        'lesson',
    )