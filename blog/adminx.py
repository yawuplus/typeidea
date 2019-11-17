from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.models import LogEntry
from .adminforms import PostAdminForm
from typeidea.custom_site import custom_site
from .models import Post, Category, Tag
from typeidea.base_admin import BaseOwnerAdmin
from xadmin.layout import Row, Fieldset
from xadmin.filters import manager
from xadmin.filters import RelatedFieldListFilter
import xadmin
from xadmin.layout import Row, Fieldset, Container


class PostInline(admin.TabularInline):
    form_layout = (
        Container(
            Row('title', 'desc'),
        )
    )
    extra = 1
    model = Post


# Register your models here.
@xadmin.sites.register(Category)
class CategoryAdmin(object):
    # inlines = [PostInline, ]
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@xadmin.sites.register(Tag)
class TagAdmin():
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status',)


# class CategoryOwnerFilter(RelatedFieldListFilter):
#     @classmethod
#     def test(cls, field, request, params, model, admin_view, field_path):
#         return field.name == 'category'
#
#     # def __init__(self, field, request, params, model, model_admin, field_path):
#     #     super().__init__(field, request, params, model, model_admin, field_path)
#     #     # 重新获取lookup_choices,根据owner过滤
#     #     self.lookup_choices = Category.objects.filter(owner=
#     #                                                   request.user).values_list('id', 'name')


# manager.register(CategoryOwnerFilter, take_priority=True)


@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status', 'created_time', 'operator', 'owner'
    ]
    list_display_links = []
    # list_filter = [CategoryOwnerFilter, ]
    search_fields = ['title', 'category__name']
    actions_on_top = True
    actions_on_bottom = True
    # 编辑页面
    # save_on_top = True
    exclude = ['owner']
    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )
    fieldsets = (
        (
            '基础配置', {
                'description': '基础配置描述',
                'fields': (
                    ('title', 'category'),
                    'status',
                ),
            }),
        (
            '内容', {
                'fields': (
                    'desc',
                    'content',
                ),
            }),
        (
            '额外信息', {
                'classes': ('wide',),
                'fields': ('tag',),
            })
    )

    # filter_horizontal = ('tags',)
    filter_vertical = ('tag',)

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('xadmin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'

    class Media:
        css = {
            'all': ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css',),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js')

    form_layout = (
        Fieldset(
            '基础信息',
            Row("title", "category"),
            'status',
            'tag',
        ),
        Fieldset(
            '内容信息',
            'desc',
            'content',
        )
    )

    # @property
    # def media(self):
    #     media = super().media
    #     media.add_js(
    #         ['https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js']
    #     )
    #     media.add_css(
    #         ['https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css']
    #     )
    #     return media
