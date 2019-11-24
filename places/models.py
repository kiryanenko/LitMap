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

    ext_id = models.CharField('Внешинй ID', max_length=255, blank=True)

    DH_CENTER_SRC = 'DH-CENTER'
    LITMAP_SRC = 'LitMap'
    SOURCES = (
        (DH_CENTER_SRC, 'DH-CENTER'),
        (DH_CENTER_SRC, 'LitMap')
    )
    source = models.CharField(choices=SOURCES, max_length=12, default=LITMAP_SRC)

    title = models.CharField('заголовок', max_length=255)
    short_text = models.TextField('короткое описание', blank=True)
    text = models.TextField('текст', blank=True)
    tags = models.ManyToManyField(Tag, related_name='places', verbose_name='теги')
    image = models.ImageField('картинка', blank=True)
    image_link = models.URLField('ссылка на картинку', blank=True)
    wiki_link = models.URLField('Ссылка на wiki', blank=True)
    x = models.FloatField('долгота')
    y = models.FloatField('широта')

    visitors = models.ManyToManyField(User, related_name='visited_places')

    def get_url(self):
        return urljoin(settings.SITE_URL, reverse('places:place_detail', args=[self.pk]))

    def __str__(self):
        return self.title
