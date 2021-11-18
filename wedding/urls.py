from user.api import MeView
from django.urls import path, include
from rest_framework import routers
from gallery.api import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import os

schema_view = get_schema_view(
   openapi.Info(
      title="Weeding Gallery API",
      default_version='v1',
      description="Submit and display images from a weeding party",
      terms_of_service="",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),


   ),
   url=os.environ.get('URL_BASE', 'https://127.0.0.1:8000'),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('gallery/pending', GalleryPendingViewSet, )
router.register('gallery', GalleryViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', MeView.as_view(), name='me'),
    path('gallery/approve/<int:pk>/', GalleryApproveViewSet.as_view({'patch': 'partial_update',}), name='gallery-approve'),
    path(r'reference/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),
]
