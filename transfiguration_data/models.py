from django.db import models
from django.core.validators import MinValueValidator

from .utils import set_default_priority


# Create your models here.


class Title(models.Model):
    title = models.CharField(max_length=60)
    priority = models.IntegerField(unique=True, default='', blank=True, null=True, validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{self.title}'


class Data(models.Model):
    input_data = models.TextField()
    output_data = models.TextField()
