
from django.contrib import admin
from django.urls import path
from news.views import home, about, contact_us
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path("/contact", contact_us)
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
