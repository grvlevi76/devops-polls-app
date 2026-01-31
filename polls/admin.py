from django.contrib import admin
from .models import Question, Student, Choice     #

# Register your models here. - edited by retard

admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Choice)


