from django.contrib import admin
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    fields = ['post_title', 'post_text', 'category', 'pub_date']
    list_display = ('post_title', 'pub_date', 'category')
    list_filter = ['category', 'pub_date']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
