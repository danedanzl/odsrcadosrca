from django.contrib import admin

from .models import Task, Attempt

# Register your models here.

admin.site.register(Task)
admin.site.register(Attempt)

