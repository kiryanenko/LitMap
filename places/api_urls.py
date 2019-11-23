from django.conf.urls import url

from places.views import PlacesViewSet, VisitedPlacesViewSet, NotVisitedPlacesViewSet, CheckInView

app_name = 'places'

urlpatterns = [
    url(r'^$', PlacesViewSet.as_view(), name='places'),
    url(r'^visited/$', VisitedPlacesViewSet.as_view(), name='visited_places'),
    url(r'^not_visited/$', NotVisitedPlacesViewSet.as_view(), name='not_visited_places'),
    url(r'^(?P<pk>\d+)/check_in/$', CheckInView.as_view(), name='check_in'),
]

