"""
Tests for portfolio app.
"""

from django.test import TestCase
from rest_framework.test import APIClient
from .models import ContactMessage, Project, Skill


class ContactMessageTestCase(TestCase):
    """Test cases for ContactMessage model and API."""

    def setUp(self):
        self.client = APIClient()

    def test_create_contact_message(self):
        """Test creating a contact message via API."""
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'Test message content'
        }
        response = self.client.post('/api/contacts/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ContactMessage.objects.count(), 1)


class ProjectTestCase(TestCase):
    """Test cases for Project model."""

    def setUp(self):
        self.project = Project.objects.create(
            title='Test Project',
            description='Test Description',
            technologies='Python, Django',
            is_featured=True
        )

    def test_project_creation(self):
        """Test creating a project."""
        self.assertEqual(self.project.title, 'Test Project')

    def test_get_projects_api(self):
        """Test retrieving projects via API."""
        response = self.client.get('/api/projects/', format='json')
        self.assertEqual(response.status_code, 200)


class SkillTestCase(TestCase):
    """Test cases for Skill model."""

    def setUp(self):
        self.skill = Skill.objects.create(
            name='Python',
            category='backend',
            proficiency=5
        )

    def test_skill_creation(self):
        """Test creating a skill."""
        self.assertEqual(self.skill.name, 'Python')
