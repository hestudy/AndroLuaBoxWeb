# Generated by Django 2.2.2 on 2019-06-09 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jxwd_fenlei',
            fields=[
                ('name', models.CharField(db_column='分类名', max_length=20, primary_key=True, serialize=False)),
                ('createtime', models.DateTimeField(auto_now_add=True, db_column='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='jxwd_context',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='标题', max_length=20)),
                ('context', models.TextField(db_column='内容')),
                ('createtime', models.DateTimeField(auto_now=True, db_column='发布时间')),
                ('fenlei', models.ForeignKey(db_column='所属分类', on_delete=django.db.models.deletion.CASCADE, to='jxwd.jxwd_fenlei')),
            ],
        ),
    ]