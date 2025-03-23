from django.urls import path, include
from . import views
urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailsAV.as_view(), name='movie-details'),
    path('stream/', views.StreamPlatformListAV.as_view(), name='stream'),
    path('stream/<int:pk>', views.StreamPlatformDetailsAV.as_view(), name='stream-details'),
    # path('reviews/', views.ReviewList.as_view(), name='review-list'),
    # path('reviews/<int:pk>', views.ReviewDetails.as_view(), name='review-details'),
    
    
    path('<int:pk>/reviews/', views.ReviewList.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetails.as_view()),
    path('reviews/', views.UserReview.as_view(), name='user-review-detail'),
    path('<int:pk>/review-create/', views.ReviewCreate.as_view()),
]
