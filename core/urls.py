from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
    
    # Shop ilovasi (bosh sahifa, savat, detallar)
    path('', include('shop.urls')),
    
    # Accounts ilovasi (login, register, logout)
    path('accounts/', include('accounts.urls')),
]

# Media fayllarni (rasmlarni) brauzerda ko'rsatish uchun
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)