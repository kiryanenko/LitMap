from rest_framework import serializers

from places.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'title', 'short_text', 'text', 'image', 'x', 'y')
