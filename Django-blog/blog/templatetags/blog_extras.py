from django import template

from ..models import Post, Category, Tag

register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_posts.html',takes_context=True)
#第一个参数是调用的html页面，第二个参数类似于视图函数里的赋值
def show_recent_posts(context,num=5):
    return {
        'recent_post_list':Post.objects.all().order_by('-created_time')[:num],
    }


@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Post.objects.dates('created_time', 'month', order='DESC'),
    }

@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all(),
    }

@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all(),
    }