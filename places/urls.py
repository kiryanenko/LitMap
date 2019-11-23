from django.conf.urls import url

from places.views import PlaceDetailView, PlacesViewSet

app_name = 'places'

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', PlaceDetailView.as_view(), name='place_detail'),
]


api_urls = [
    url(r'^$', PlacesViewSet.as_view(), name='places'),
]
