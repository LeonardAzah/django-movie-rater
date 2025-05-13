from django.urls import path
# from .views import movie_list, movie_details
from .views import MovieListAV, MovieDetailAV, StreamPlatformList, SteamPlatformDetail

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie_list' ),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie_details'),
    path('stream/', StreamPlatformList.as_view(), name='platform_list'),
    path('stream/<int:pk>/', SteamPlatformDetail.as_view(), name='platform_details'),

]
