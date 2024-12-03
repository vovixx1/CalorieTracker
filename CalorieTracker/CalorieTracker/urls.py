from django.contrib import admin
from django.urls import path, include  # include is necessary for the app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Add this line to include accounts app URLs
    path('', include('myapp.urls')),  # Include myapp URLs
]
