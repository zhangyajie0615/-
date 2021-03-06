# Generated by Django 2.2.3 on 2020-03-17 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200308_1444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pictest',
            options={'verbose_name': '上传文件', 'verbose_name_plural': '上传文件'},
        ),
        migrations.AddField(
            model_name='pictest',
            name='music',
            field=models.FileField(blank=True, default='', upload_to='mus', verbose_name='音乐'),
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='pictest',
            name='pic',
            field=models.ImageField(blank=True, default='', upload_to='img', verbose_name='图片'),
        ),
    ]
