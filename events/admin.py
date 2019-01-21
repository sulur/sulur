from django.contrib import admin
from events.models import Category, Events
# Register your models here.
admin.site.register(Category)
admin.site.register(Events)