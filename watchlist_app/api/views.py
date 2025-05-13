from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import WatchList, StreamPlatform
from .serializers import MovieSerializer, StreamPlatformSerializer

from rest_framework.views import APIView

class StreamPlatformList(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class SteamPlatformDetail(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(platform)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except StreamPlatform.DoesnotExist:
            return Response({'error': 'Streaming platform not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MovieListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class MovieDetailAV(APIView):

    def get(self,request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(selfself, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response({'msg': 'Movie deleted'}, status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#         return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     if request.method == 'PUT':
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK )
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         movie.delete()
#         return Response({'msg':'Movie deleted'}, status=status.HTTP_204_NO_CONTENT)