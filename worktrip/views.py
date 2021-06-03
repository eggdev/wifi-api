from rest_framework import viewsets, permissions
from worktrip.models import Location
from worktrip.serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Location.objects.all().order_by("-created_date")
    serializer_class = LocationSerializer
