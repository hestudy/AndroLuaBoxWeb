from django.db import models

# Create your models here.
class classification(models.Model):
    name = models.CharField(max_length=20,db_column='分类',primary_key=True)
    createtime = models.DateTimeField(auto_now_add=True,db_column='建立时间')
    updatetime = models.DateTimeField(auto_now=True,db_column='最近修改时间')

class tutorial(models.Model):
    classification = models.ForeignKey('classification',on_delete=models.CASCADE,db_column='所属分类')
    title = models.CharField(max_length=20,db_column='标题',primary_key=True)
    context = models.TextField(db_column='教程')
    createtime = models.DateTimeField(auto_now_add=True, db_column='建立时间')
    updatetime = models.DateTimeField(auto_now=True, db_column='最近修改时间')

class runtut(models.Model):
    tutorial = models.ForeignKey('tutorial',on_delete=models.CASCADE,db_column='所属标题')
    title = models.CharField(max_length=20, db_column='标题', primary_key=True)
    context = models.TextField(db_column='教程')
    createtime = models.DateTimeField(auto_now_add=True, db_column='建立时间')
    updatetime = models.DateTimeField(auto_now=True, db_column='最近修改时间')