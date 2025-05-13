from rest_framework import serializers
from ..models import WatchList, StreamPlatform


class MovieSerializer(serializers.ModelSerializer):
     class Meta:
          model = WatchList
          fields = "__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
     watchlist = MovieSerializer(many=True, read_only=True)
     class Meta:
          model = StreamPlatform
          fields = "__all__"



