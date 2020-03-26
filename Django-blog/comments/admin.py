from django.contrib import admin
from .models import Comment, Notice
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'post', 'created_time']
    fields = ['name', 'email', 'url', 'text', 'post']

# Register your models here. 为了让admin界面管理某个数据库模型，我们先注册该数据模型到admin


admin.site.register(Comment, CommentAdmin)
admin.site.register(Notice)