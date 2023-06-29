from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Workstation)
admin.site.register(models.Schedule)
