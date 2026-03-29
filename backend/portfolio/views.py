"""
Views for portfolio API.
"""

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from django.conf import settings

from .models import ContactMessage, Project, Skill
from .serializers import ContactMessageSerializer, ProjectSerializer, SkillSerializer


class ContactMessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint for contact messages.
    POST to submit a contact form.
    GET/LIST only for admin.
    """
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        """Allow anyone to create, restrict others to admin."""
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        """Create a new contact message and send email."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Send email notification
        try:
            send_mail(
                subject=f"New Contact Form: {serializer.data['subject']}",
                message=f"From: {serializer.data['name']} ({serializer.data['email']})\n\n{serializer.data['message']}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=True,
            )
        except Exception:
            pass  # Silently fail email sending

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for projects.
    GET to retrieve all projects.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured projects."""
        featured_projects = Project.objects.filter(is_featured=True)
        serializer = self.get_serializer(featured_projects, many=True)
        return Response(serializer.data)


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for skills.
    GET to retrieve all skills.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get skills grouped by category."""
        categories = {}
        for category, display in Skill.CATEGORY_CHOICES:
            skills = Skill.objects.filter(category=category)
            categories[display] = SkillSerializer(skills, many=True).data
        return Response(categories)
