from django.test import TestCase
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from transfiguration_data.models import Title, Data  # замените "your_app" на актуальное имя вашего приложения


class TitleModelTest(TestCase):
    def test_create_title(self):
        title = Title.objects.create(title='Test Title', priority=1)

        self.assertEqual(Title.objects.count(), 1)

        self.assertEqual(title.title, 'Test Title')
        self.assertEqual(title.priority, 1)

        self.assertEqual(str(title), 'Test Title')


class DataModelTest(TestCase):
    def test_create_data(self):
        data = Data.objects.create(input_data='input', output_data='output')

        self.assertEqual(Data.objects.count(), 1)

        self.assertEqual(data.input_data, 'input')
        self.assertEqual(data.output_data, 'output')
