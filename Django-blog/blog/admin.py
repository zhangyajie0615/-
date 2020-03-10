from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Category, Tag, PicTest


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','category','author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
#第一个request是此次HTTP请求对象，第二个obj此次关联对象实例user；super() 函数是用于调用父类(超类)的一个方法


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(PicTest)