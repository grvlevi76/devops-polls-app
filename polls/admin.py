from django.contrib import admin
from .models import Question, random, Choice     #

# Register your models here. - edited by retard

admin.site.register(Question)
admin.site.register(random)
admin.site.register(Choice)


