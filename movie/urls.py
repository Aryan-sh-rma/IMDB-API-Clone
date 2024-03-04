
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('watchmate.api.urls')),
    path('account/', include('user_app.api.urls')),
]
