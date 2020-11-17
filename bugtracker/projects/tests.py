from django.test import TestCase, Client
from .models import Project
from django.contrib.auth.models import User, AnonymousUser
from users.models import Profile
from django.urls import reverse

# Create your tests here.

class ProjectTestCase(TestCase):
    def setUp(self):
        # testuser1 = User.objects.create_user(username='testauto', email='jacob@testauto.com', password='top_secret')
        # Profile.objects.create(user=testuser1)
        p1 = Project.objects.create(name="automated test", proj_type="D")
        # p1.editors.set(AnonymousUser())
        p2 = Project.objects.create(name="automated test2", proj_type="P")
        # p2.editors.set(AnonymousUser())
        self.client = Client()


    def test_project_has_type(self):
        """Projects have a defined type"""
        dev = Project.objects.get(name="automated test")
        print_o = Project.objects.get(name="automated test2")
        self.assertEqual(dev.proj_type, 'D')
        self.assertEqual(print_o.proj_type, 'P')

    def test_bug_list_displays(self):
        response = self.client.get('/projects/bugs/')
        self.assertTrue(response.status_code == 200 or response.status_code == 302)
        # self.assertEqual(len(response.context['customers']), 5)