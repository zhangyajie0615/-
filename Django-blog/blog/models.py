from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    """
    django 要求模型必须继承 models.Model类
    Category 只需要一个简单的分类名 name就可以
    CharField指定了分类名name的数据类型，CharField 是字符型
    CharField的max_length 参数指其最大长度，超过这个长度的分类名就不能被存入数据库
    日期时间类型 DateTimeField、整数类型 IntegerField
    """
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    标签Tag也比较简单，和Category一样
    一定要继承models.Model类
    """
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name='标签'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class Post(models.Model):
    """
    文章的数据库稍微复杂一点，主要是涉及的字段更多
    """
    # 文章标题
    title=models.CharField('标题',max_length=70)
    # 文章正文，我们使用了TextField
    # 储存比较短的字符串可以使用CharField，但对于文章正文来说会是一大段文本，因此使用TextField来存储大段文本。
    body=models.TextField('正文')

    # 这两个列分别表示文章的创建时间和最后一次的修改时间，存储时间的字段用DateTimeField类型。
    created_time=models.DateField('创建时间', default=timezone.now)
    modified_time=models.DateField('修改时间')

    # 文章摘要，可以没有文章，但默认情况下CharField要求我们必须存入数据，否则就会报错
    # 指定CharField的blank=True参数值后就可以允许空值了
    excerpt=models.CharField('摘要',max_length=200,blank=True)

    # 我们将分类与标签的模型定义在上面。
    # 这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    # 我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey即一对多的关系
    # 在django2.0以后Foreignkey必须传入on_delete参数，来关联数据行为：分类被删么分类下所有的文章都会被删除
    # 对于标签来说就是：一个标签有多个文章，一个文章也可以有多个标签，是多对多的关系所以使用ManyToManyField
    # 我们规定文章可以没有标签，所以因标签 tags 指定了 blank=True。
    category=models.ForeignKey(Category,verbose_name='分类',on_delete=models.CASCADE)
    Tags=models.ManyToManyField(Tag,verbose_name='标签',blank=True)

    # User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是
    # django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和
    # Category 类似。
    author=models.ForeignKey(User,verbose_name='作者',on_delete=models.CASCADE)
    def save(self,*args,**kwargs):
        self.modified_time=timezone.now()
        super().save(*args,**kwargs)

    class Meta:
        verbose_name='文章'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title


    #自定义 get_absolute_url 方法
    #记得从 django.urls 中导入reverse的函数
    #def get_absolute_url(self):
        #return reverse('blog:detail',kwargs={'pk':self.pk})