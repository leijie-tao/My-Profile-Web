"""
Django admin configuration for portfolio app.
"""

from django.contrib import admin
from .models import ContactMessage, Project, Skill


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['created_at', 'is_read']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    fields = ['name', 'email', 'subject', 'message', 'is_read', 'created_at']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'created_at']
    list_filter = ['is_featured', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'description')
        }),
        ('Links', {
            'fields': ('github_url', 'live_url', 'image_url')
        }),
        ('Details', {
            'fields': ('technologies', 'is_featured')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency']
    list_filter = ['category', 'proficiency']
    search_fields = ['name']
    fields = ['name', 'category', 'proficiency']
