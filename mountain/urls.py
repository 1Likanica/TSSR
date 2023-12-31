from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from perevalapp.views import PerevalViewSet
from .yasg import urlpatterns as doc_urls


router = routers.DefaultRouter()
router.register(r'pereval', PerevalViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('submitData/', include(router.urls)),
]

urlpatterns += doc_urls