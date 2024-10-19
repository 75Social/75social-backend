from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social75.urls')), 
    path('post/', views.postData),  # Includes the helloworld app's URLs
]
