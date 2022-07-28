from django.contrib import admin

# Register your models here.
from .models import Categories, ReadMore

admin.site.register(Categories)
admin.site.register(ReadMore)