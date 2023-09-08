from django.test import TestCase
from .forms import CommentForm


class FormTest(TestCase):

    def test_comment_form_valid(self):
        form_data = {'name': 'Tester', 'email': 'home@now.com', 'body': 'Test text'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid(self):
        form_data = {}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())