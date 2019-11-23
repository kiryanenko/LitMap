from django.views.generic import DetailView
from rest_framework import permissions
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from places.models import Place
from places.serializers import PlaceSerializer


class PlaceDetailView(DetailView):
    template_name = 'places/place_detail.html'
    model = Place


class PlacesViewSet(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class VisitedPlacesViewSet(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(visitors=self.request.user)


class NotVisitedPlacesViewSet(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.exclude(visitors=self.request.user)


class CheckInView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk, *args, **kwargs):
        place = get_object_or_404(Place, pk=pk)
        request.user.visited_places.add(place)
        return Response({}, status=200)
