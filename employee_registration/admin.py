from django.contrib import admin
from .models import *

# Register your models here.

class EmpRegistrationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number', 'email', 'address','position']
    list_filter = ['name']

class PositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class EmpDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number', 'email', 'address']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'comment']

class ShopingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email','conutry']
    list_filter=['district']

admin.site.register(EmpRegistration, EmpRegistrationAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(EmpDetails,EmpDetailsAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(ShoopingCheckOut,ShopingAdmin)
