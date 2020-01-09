from django.contrib import admin
from .models import jxwd_context,jxwd_fenlei
# Register your models here.
@admin.register(jxwd_context)
class jxwd_contextAdmin(admin.ModelAdmin):
    list_display = ['title','fenlei','context','createtime']

@admin.register(jxwd_fenlei)
class jxwd_fenleiAdmin(admin.ModelAdmin):
    list_display = ['name','createtime']