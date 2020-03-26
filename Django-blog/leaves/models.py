from django.db import models
from django.utils import timezone


class Leave(models.Model):
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text