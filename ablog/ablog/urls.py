from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter

from theblog.views import ProfileViewSet, PostViewSet

router = SimpleRouter()
router.register(r'api_profiles', ProfileViewSet)
router.register(r'api_posts', PostViewSet)


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('theblog.urls')),
                  path('members/', include('django.contrib.auth.urls')),
                  path('members/', include('members.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls