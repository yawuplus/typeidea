from django.contrib import admin
from .models import Sidebar, Link
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
import xadmin


# Register your models here.
@xadmin.sites.register
class LinkAdmin():
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')


@xadmin.sites.register
class SidebarAdmin():
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')
