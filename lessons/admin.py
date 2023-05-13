from django.contrib import admin
from .models import(
    LessonTeacher,
    LessonType,
    Lesson,
    Banner
)
# Register your models here.
admin.site.register(LessonTeacher)
admin.site.register(LessonType)
admin.site.register(Lesson)
admin.site.register(Banner)