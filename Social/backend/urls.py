from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social75.urls')),  # Includes the helloworld app's URLs
]