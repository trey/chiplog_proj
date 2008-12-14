from django.contrib import admin
from django.contrib.redirects.models import Redirect
from tagging.models import Tag, TaggedItem
from chiplog.models import Entry
from chiplog.admin import EntryAdmin

class AdminSite(admin.AdminSite):
    pass

site = AdminSite()

site.register(Entry, EntryAdmin)
site.register(Redirect)
site.register(Tag)
site.register(TaggedItem)
