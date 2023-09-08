from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class ModelsTest(TestCase):

    def test_create_post(self):
        self.user = User.objects.create_user(username='tester', password='password')