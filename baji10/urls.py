
from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('client.urls')),
    path('account/', include('account.urls')),
    path('superadmin/', include('superadmin.urls')),
    path('game-control/', include('game_control.urls')),
    path('others/', include('others.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)