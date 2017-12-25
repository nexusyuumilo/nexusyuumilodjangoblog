from django.views import generic
from .models import Post, Category


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'
    model = Post

    def get_context_data(self, *args, **kwargs):
        """最新5記事を返す"""
        context = super().get_context_data(*args, **kwargs)
        context['category_list'] = Category.objects.all()
        return context


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category_list'] = Category.objects.all()
        return context


class CategoryView(generic.DetailView):
    model = Post
    model = Category
    template_name = 'blog/category.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category_list'] = Category.objects.all()
        return context
