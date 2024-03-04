from rest_framework import serializers
from watchmate.models  import WatchList,StreamPlatform,Review



class ReviewSerializer(serializers.ModelSerializer):
    name=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Review
        exclude=('watchlist',)
        
        
 
# Serilaizers    watch list
class WatchListSerializer(serializers.ModelSerializer):
    platform=serializers.CharField(source='platform.name')
    
    class Meta:
        model = WatchList
        fields ='__all__'
        
        
# serializer for  Streaming Platforms
class StreamPlatformSerializer(serializers.ModelSerializer):
    # realated name in watchlist model
    watchlist=WatchListSerializer(many=True,read_only=True)
    class Meta:
        model = StreamPlatform
        fields ='__all__'
        



        
        
    
        
    
     