from django.urls import path, include
# from .views import movie_list, movie_details
from rest_framework.routers import DefaultRouter
from .views import MovieListAV, MovieDetailAV, StreamPlatformList, SteamPlatformDetail, ReviewList, ReviewDetail, \
    ReviewCreate, StreamPlatformVS, UserReview

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='stream_platform')
urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie_list' ),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie_details'),
    path('', include(router.urls)),
    # path('stream/', StreamPlatformList.as_view(), name='platform_list'),
    # path('stream/<int:pk>/', SteamPlatformDetail.as_view(), name='platform_details'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='reviews-list' ),
    path('<int:pk>/reviews-create/', ReviewCreate.as_view(), name='reviews-create' ),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='reviews-details'),
    path('reviews/',UserReview.as_view(), name='user-reviews' ),

]
