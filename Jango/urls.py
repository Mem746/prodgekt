from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('registration.urls')),  # Add this line
    path('home/', include('home.urls')),  # Add this line
]
