from django.contrib import admin
from chiplog.models import Entry
from chiplog.admin import EntryAdmin

class AdminSite(admin.AdminSite):
    pass

site = AdminSite()

site.register(Entry, EntryAdmin)
