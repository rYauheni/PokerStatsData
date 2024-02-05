from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get(self):
        response = self.client.get(reverse('index_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'transfiguration_data/index.html')

    def test_post_request_redirects_on_valid_form_submission(self):
        response = self.client.post(reverse('index_url'), data={'input_data': 'value'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['input_data']['input_data'], 'value')
        self.assertTrue(self.client.session['existence'])


class TransfigurationViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_404(self):
        response = self.client.get(reverse('transfiguration_url'))
        self.assertEqual(response.status_code, 404)
