from rest_framework import serializers
from worktrip.models import Venue


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venue
        fields = ["name", "download_speed", "upload_speed", "venue_type", "venue_url"]
