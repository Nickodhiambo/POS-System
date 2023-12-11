from django.contrib import admin
from django.contrib.admin import AdminSite
from posApp.models import Category, Products, Sales

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Sales)
