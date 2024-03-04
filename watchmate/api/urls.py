
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from watchmate.api.views import (WatchListAV,WatchDetailAV,ReviewList,ReviewDetails,
                                 ReviewCreate,StreamPlatformVS,UserReview)


router=DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')

urlpatterns = [
    path('list/',WatchListAV.as_view(),name='watch-list'),
    path('<int:pk>/',WatchDetailAV.as_view(),name='watch-detail'),
    
    
    path('<int:pk>/review-create',ReviewCreate.as_view(),name='review-create'),
    path('<int:pk>/reviews/',ReviewList.as_view(),name='review-list'),
    path('review/<int:pk>',ReviewDetails.as_view(),name='review-details'),
    path('reviews/',UserReview.as_view(),name='user-review-details'),
     
    path('',include(router.urls)),
]

