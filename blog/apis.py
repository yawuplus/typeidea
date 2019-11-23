from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Post, Category
from .serializers import (
    PostSerializer, PostDetailSerializer,
    CategorySerializer, CategoryDetailSerializer)
from rest_framework.decorators import api_view


# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
class PostViewSet(viewsets.ModelViewSet):
    """提供文章接口"""
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    permission_classes = [AllowAny]  # 写入时校验

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)
