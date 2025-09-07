from django.contrib import admin
from .models import About, Skill, Project, ContactMessage

admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(ContactMessage)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')