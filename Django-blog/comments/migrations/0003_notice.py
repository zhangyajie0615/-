# Generated by Django 2.2.3 on 2020-03-26 03:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20200305_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='标题')),
                ('text', models.TextField(verbose_name='内容')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '公告',
                'verbose_name_plural': '公告',
                'ordering': ['-created_time'],
            },
        ),
    ]
