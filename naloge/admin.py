from django.contrib import admin

from .models import Task, Attempt, MchoiceTask, MchoiceQuestion, MchoiceAnswer

admin.site.register(Task)
admin.site.register(Attempt)

admin.site.register(MchoiceTask)
admin.site.register(MchoiceQuestion)
admin.site.register(MchoiceAnswer)

