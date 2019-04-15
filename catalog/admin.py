# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category , Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name'  ,'price' , 'old_price',  'is_active')
    list_per_page = 50
    ordering = ['created_at']
    search_fields = ['name' , 'price' , 'old_price' , 'meta_keywords' , 'meta_description' , 'description']
    exclude = ('created_at' , 'updated_at')
    prepopulated_fields = {'slug':('name',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_per_page = 20
    search_fields = ['name', 'description' , 'meta_keywords' , 'meta_description' ,]
    exclude = ('created_at', 'updated_at')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category , CategoryAdmin)
admin.site.register(Product , ProductAdmin)