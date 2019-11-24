import requests
from django.core.management import BaseCommand

from places.models import Place


class Command(BaseCommand):
    help = 'Update dh-center places'

    def handle(self, *args, **options):
        url = 'https://api.st-retrospect.dh-center.ru/graphql'

        data = r'{"query":"query {\n  locations {\n    id\n    name\n    description\n    wikiLink\n    coordinateX\n    coordinateY\n    mainPhotoLink\n  }\n}"}'
        r = requests.post(url, data=data, headers={
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Connection': 'keep-alive'
        })
        print(r.text)
        resp = r.json()

        for location in resp['data']['locations']:
            title = location.get('name', {}).get('ru', '')
            if not title:
                title = ''

            wiki_link = location.get('wikiLink', '')
            if len(wiki_link) > 200:
                wiki_link = ''

            img = location.get('mainPhotoLink', '')
            if len(img) > 200:
                img = ''

            text = location.get('description', {}).get('ru', '')
            if not text:
                text = ''

            x = location['coordinateX']
            y = location['coordinateY']
            if x is None or y is None:
                continue

            print(title)
            Place.objects.update_or_create(source=Place.DH_CENTER_SRC, ext_id=location['id'], defaults={
                'title': title[:255],
                'text': text,
                'short_text': text,
                'wiki_link': wiki_link,
                'image_link': img,
                'x': x,
                'y': y,
            })
