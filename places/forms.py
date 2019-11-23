from urllib.parse import urljoin

from django import forms
from django.conf import settings
from webpush import send_user_notification

from places.models import Place


class PlacePushForm(forms.Form):
    place = forms.ModelChoiceField(queryset=Place.objects.all())
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    select_across = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, users, *args, **kwargs):
        super(PlacePushForm, self).__init__(*args, **kwargs)
        self.users = users

    def save(self):
        place = self.cleaned_data['place']

        payload = {
            "head": place.title,
            "body": place.short_text,
            'url': place.get_url(),
        }
        if place.image.name:
            payload['icon'] = urljoin(settings.SITE_URL, place.image.name)

        for user in self.users:
            send_user_notification(user=user, payload=payload)
