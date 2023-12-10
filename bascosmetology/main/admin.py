from django.contrib import admin
from .models import Category, Records, Procedure

# Register your models here.
admin.site.register(Category)
admin.site.register(Records)
admin.site.register(Procedure)
