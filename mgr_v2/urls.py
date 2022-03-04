from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from proba_strzelnicza import views as shot_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", shot_views.index, name="index"),
    path("<int:sample_id>", shot_views.shot, name="proba_strzelnicza"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
