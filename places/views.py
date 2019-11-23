from django.views.generic import DetailView

from places.models import Place


class PlaceDetailView(DetailView):
    template_name = 'places/place_detail.html'
    model = Place
