from rest_framework import serializers
from ..models import WatchList, StreamPlatform, Review




class ReviewSerializer(serializers.ModelSerializer):
    review_author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ['watchlist']


class WatchListSerializer(serializers.ModelSerializer):
    
    reviews = ReviewSerializer(many=True, read_only=True)        #  related field
    
    class Meta:
        model = WatchList
        fields = '__all__'
        # exclude = ['active']
        


class StreamPlatformSerializer(serializers.ModelSerializer):
    
    watchlist = WatchListSerializer(many=True, read_only=True)        #  related field
    # watchlist = serializers.StringRelatedField(many=True)             #  string related field
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-details'
    # )
    
    class Meta:
        model = StreamPlatform 
        fields = '__all__'
        # extra_kwargs = {
        #     'url': {'view_name': 'stream-details', 'lookup_field': 'pk'}
        # }






# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=50)
#     description = serializers.CharField(max_length=200)
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     #adding validation
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and Description should be different')
#         return data
    
    
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name is too short')
#         return value