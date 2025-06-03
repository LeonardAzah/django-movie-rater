from rest_framework import serializers
from ..models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
     review_user = serializers.StringRelatedField(read_only=True)

     class Meta:
          model = Review
          exclude = ('watchlist',)
          # fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
     # reviews = ReviewSerializer(many=True, read_only=True)
     platform = serializers.CharField(source='platform.name')
     class Meta:
          model = WatchList
          fields = "__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
     # watchlist = MovieSerializer(many=True, read_only=True)
     class Meta:
          model = StreamPlatform
          fields = "__all__"




