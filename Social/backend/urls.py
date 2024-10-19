from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/social75/', include('social75.urls')),  # Including app-level URLs from social75
    path('api/backend/', include('backend.urls')),    # Including app-level URLs from backend
]
