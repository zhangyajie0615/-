# Generated by Django 2.2.7 on 2020-03-26 06:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liuyan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='内容')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '留言',
                'verbose_name_plural': '留言',
                'ordering': ['-created_time'],
            },
        ),
    ]