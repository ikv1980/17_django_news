from django.contrib import admin
from .models import Point, userMessage, aboutMessage, News

# Register your models here.
admin.site.register(Point)
admin.site.register(userMessage)
admin.site.register(aboutMessage)
admin.site.register(News)
