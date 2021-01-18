from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('siteboss.urls')),
] + static(settings.STATIC_URL, boss=settings.STATIC_ROOT)
