from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from music.admin import music_admin

urlpatterns = [
    path("wolduadmin/", admin.site.urls),
    path("admin/", music_admin.urls),
    path("api/", include("music.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)