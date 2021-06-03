from rest_framework import viewsets, permissions
from worktrip.models import Venue
from worktrip.serializers import VenueSerializer


class VenueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Venue.objects.all().order_by("-created_date")
    serializer_class = VenueSerializer
