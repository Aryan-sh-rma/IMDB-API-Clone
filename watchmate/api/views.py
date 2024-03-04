from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView       
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


#imprts from app 
from watchmate.models import WatchList,StreamPlatform,Review
from watchmate.api.serializers import (WatchListSerializer,
                                       StreamPlatformSerializer,
                                       ReviewSerializer)

from watchmate.api.permissions import(IsAdminOrReadOnly,
                                      IsReviewUserOrReadonly)




#---------------------------------ALL IMPORTS ---------------------------------------

class UserReview(generics.ListAPIView):
        serializer_class=ReviewSerializer
        permission_classes=[IsAuthenticated]
        def get_queryset(self):
            username = self.request.query_params.get('username',None)
            all_reviews=Review.objects.filter(reviewer__username=username)
            return all_reviews

# Gives a review detail by its review id  [stream/review/6] 
class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
        queryset=Review.objects.all()
        serializer_class=ReviewSerializer
        permission_classes = [IsReviewUserOrReadonly]




#list of all review of a particular movie ['<int:pk>/review']

class ReviewList(generics.ListAPIView):
        serializer_class=ReviewSerializer
        permission_classes=[IsAuthenticated]
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['reviewer__username','active']
        def get_queryset(self):
            pk=self.kwargs['pk']
            all_reviews=Review.objects.filter(watchlist=pk)
            return all_reviews
            
            
                
        
        


# Making review for particular movie.  [stream/<int:pk>/review-create]   
class ReviewCreate(generics.CreateAPIView):
        serializer_class=ReviewSerializer
        permission_classes = [IsAuthenticated]
        
        
        def get_queryset(self):
            return Review.objects.all() 
        
        
        def perform_create(self,serializer):
            pk=self.kwargs.get('pk')
            watchlist=WatchList.objects.get(pk=pk)
            
            review_user=self.request.user
            review_queryset=Review.objects.filter(watchlist=watchlist,reviewer=review_user)
            
            if review_queryset.exists():
                raise ValidationError("OOPS !Looks like you have already reviewed this movie ")
            
            
            if watchlist.number_rating ==0:
                watchlist.avg_rating=serializer.validated_data['rating']
            else:
                watchlist.avg_rating=(watchlist.number_rating+serializer.validated_data['rating'])/2
                
            watchlist.number_rating+=1
            watchlist.save()
            serializer.save(watchlist=watchlist,reviewer=review_user)


# All movies [list/]
class WatchListAV(APIView):
    permission_classes=[IsAdminOrReadOnly]
    
    def get(self,request):
        movies=WatchList.objects.all()
        serializer=WatchListSerializer(movies,many=True)
        return Response(serializer.data)
    
   
    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
        
# For particular movie details.  [2/]       
class WatchDetailAV(APIView):
    permission_classes=[IsAdminOrReadOnly]
    def get(self,request,pk):
        try:
           movie=WatchList.objects.get(pk=pk)
           
        except WatchList.DoesNotExist:
            return Response({'error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=WatchListSerializer(movie)
        return Response(serializer.data)
    
    
    def put(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
    def delete(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
#-----------------------------------------------------------------------------------------------------------   
 
 
 
# streaming platform
class StreamPlatformVS(viewsets.ModelViewSet):
    permission_classes=[IsAdminOrReadOnly]
    queryset = StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer








            
            
            
        

    

     
    
    
        
        
        
        
        
        
            
        


