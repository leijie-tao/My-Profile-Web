"""
Serializers for portfolio API.
"""

from rest_framework import serializers
from .models import ContactMessage, Project, Skill


class ContactMessageSerializer(serializers.ModelSerializer):
    """Serializer for contact messages."""

    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'subject', 'message', 'created_at', 'is_read']
        read_only_fields = ['id', 'created_at', 'is_read']


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for projects."""

    technologies = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'technologies', 'github_url',
                  'live_url', 'image_url', 'is_featured', 'created_at']
        read_only_fields = ['id', 'created_at']

    def get_technologies(self, obj):
        """Convert comma-separated technologies to list."""
        return [tech.strip() for tech in obj.technologies.split(',')]


class SkillSerializer(serializers.ModelSerializer):
    """Serializer for skills."""

    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Skill
        fields = ['id', 'name', 'category', 'category_display', 'proficiency']
        read_only_fields = ['id']
