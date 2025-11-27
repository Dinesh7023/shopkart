from django.contrib import admin
from .models import *
# from dental.models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
# admin.site.register(customers)
# Register your models here.
