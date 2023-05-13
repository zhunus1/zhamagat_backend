from django.contrib import admin
from .models import (
    Region,
    City,
    Mosque
)

# Register your models here.
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Mosque)