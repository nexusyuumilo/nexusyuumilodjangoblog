from django.db import models
from django.utils import timezone


class Category(models.Model):
    category_name = models.CharField('カテゴリ名', max_length=10)

    def __str__(self):
        return self.category_name

    def get_posts(self):
        posts = Post.objects.filter(category=self)
        return posts


class Post(models.Model):
    post_title = models.CharField('タイトル', max_length=30)
    post_text = models.TextField(default="")
    pub_date = models.DateTimeField('公開日', default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title
