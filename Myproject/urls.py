from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include  # เพิ่่ม urls.py ใน MyWebsite
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyWebsite.urls')),  # เพิ่ม urls.py ใน Mywebsite
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
