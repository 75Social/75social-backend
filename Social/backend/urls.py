from django.contrib import admin
from django.urls import path, include
from social75 import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social75.urls')), 
    path('post/', views.index),  # Includes the helloworld app's URLs
]
