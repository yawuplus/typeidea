from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag, Category
from config.models import Sidebar
from django.views.generic import DetailView, ListView


# Create your views here.

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'


# class PostListView(ListView):
#     queryset = Post.latest_posts()
#     # 每页数量
#     paginate_by = 1
#     context_object_name = 'post-list'  # 如果不设置此项，在模板中需要使用object_list变量
#     template_name = 'blog/list.html'


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None
    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posts()

    context = {
        'category': category,
        'tag': tag,
        'post_list': post_list,
        'sidebars': Sidebar.get_all(),
    }
    context.update(Category.get_navs())
    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id=None):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    context = {
        'post': post,
        'sidebars': Sidebar.get_all(),
    }
    context.update(Category.get_navs())
    return render(request, 'blog/detail.html', context={'post': post})
