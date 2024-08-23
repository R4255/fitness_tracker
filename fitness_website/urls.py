from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include allauth URLs for authentication
    path('', include('fitness_app.urls')),       # Include URLs from your app
]