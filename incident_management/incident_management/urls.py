from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('api/', include('api.urls')),  # Include API URLs from the 'api' app
    path('', RedirectView.as_view(url='api/', permanent=True)),  # Redirect root to 'api/'
]
