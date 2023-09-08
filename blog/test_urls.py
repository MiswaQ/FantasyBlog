from django.test import TestCase
from django.urls import reverse


class UrlsTest(TestCase):

    def test_home_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url(self):
        response = self.client.get(reverse('post_detail', args=['test-post']))

    def test_post_like_url(self):
        response = self.client.post(reverse('post_like', args=[1]))

    def test_delete_url(self):
        response = self.client.post('delete', args=['test-post'])

    def test_edit_url(self):
        response = self.client.get(reverse('edit_comment', args=[1]))
