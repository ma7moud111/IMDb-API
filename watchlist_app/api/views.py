from ..models import WatchList, StreamPlatform, Review
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from .permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly






class WatchListAV(APIView):
        
    def get(self, request):
        watchlists = WatchList.objects.all()
        serializer = WatchListSerializer(watchlists, many=True)
        return Response(serializer.data)    


    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class WatchDetailsAV(APIView):
    
    def get(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'Watch list not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        watchlist = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        watchlist = WatchList.objects.get(pk=pk)
        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



################################################################################################


class StreamPlatformListAV(APIView):
    
    def get(self, request):
        stream_platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(stream_platforms, many=True)
        return Response(data=serializer.data)
    
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    



class StreamPlatformDetailsAV(APIView):
    
    def get(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"error": "platform not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializer(stream_platform)
        return Response(data=serializer.data)
    
    
    def put(self, request, pk):
        stream_platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(stream_platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        stream_platform = StreamPlatform.objects.get(pk=pk)
        stream_platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
        

################################################################################################


# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    


# class ReviewDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()
    
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        movie = WatchList.objects.get(pk=pk)
        
        review_author = self.request.user
        review_queryset = Review.objects.filter(watchlist=movie, review_author=review_author)
        if review_queryset.exists():
            raise ValidationError("You already created a review for this movie!")
        
        serializer.save(watchlist=movie, review_author=review_author)
        


class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]
    
    

################################################################################################


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
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)




# @api_view(['GET', 'PUT', 'DELETE' ])
# def movie_details(request, pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#         return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
    
#     if request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



