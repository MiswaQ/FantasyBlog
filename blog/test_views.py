from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment


class ViewsTest(TestCase):

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[1]))

    def test_post_like_view(self):
        response = self.client.get('post_like')
        self.client.login(username='test', password='password')

    def test_post_edit_view(self):
        response = self.client.get('edit_comment')
        self.client.login(username='test', password='password')

    def test_post_delete_view(self):
        response = self.client.get('delete_comment')
        self.client.login(username='test', password='password')
