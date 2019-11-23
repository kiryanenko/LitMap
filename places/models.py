from urllib.parse import urljoin

from django.conf import settings
from django.db import models
from django.urls import reverse

from core.models import User


class Tag(models.Model):
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    name = models.CharField('Название', max_length=200)
    subscribers = models.ManyToManyField(User, verbose_name='подписчики')

    def __str__(self):
        return self.name


class Place(models.Model):
    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'

    title = models.CharField('заголовок', max_length=255)
    short_text = models.TextField('короткое описание', blank=True)
    text = models.TextField('текст', blank=True)
    tags = models.ManyToManyField(Tag, related_name='places', verbose_name='теги')
    image = models.ImageField('картинка', blank=True)
    x = models.FloatField('долгота')
    y = models.FloatField('широта')

    def get_url(self):
        return urljoin(settings.SITE_URL, reverse('places:place_detail', args=[self.pk]))

    def __str__(self):
        return self.title
