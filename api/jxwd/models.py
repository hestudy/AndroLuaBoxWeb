from django.db import models

# Create your models here.
class jxwd_fenlei(models.Model):
    name = models.CharField(max_length=20,db_column='分类名',primary_key=True)
    createtime = models.DateTimeField(auto_now_add=True,db_column='创建时间')

class jxwd_context(models.Model):
    title = models.CharField(max_length=20,db_column='标题',primary_key=True)
    fenlei = models.ForeignKey(jxwd_fenlei,db_column='所属分类',on_delete=models.CASCADE)
    context = models.TextField(db_column='内容')
    createtime = models.DateTimeField(auto_now=True,db_column='发布时间')