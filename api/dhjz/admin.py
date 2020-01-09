from django.contrib import admin
from .models import tutorial,classification,runtut
# Register your models here.
@admin.register(tutorial)
class tutadmin(admin.ModelAdmin):
    list_display = ['classification','title','context','createtime','updatetime']

@admin.register(classification)
class claadmin(admin.ModelAdmin):
    list_display = ['name','createtime','updatetime']

@admin.register(runtut)
class runadmin(admin.ModelAdmin):
    list_display = ['tutorial','title','context','createtime','updatetime']