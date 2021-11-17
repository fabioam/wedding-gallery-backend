from rest_framework import permissions, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from . import serializers
from .models import Gallery


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.approved()
    serializer_class = serializers.GallerySerializer
    http_method_names = ['get', 'post', ]
    parser_classes = (MultiPartParser, FormParser,)


class GalleryPendingViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.notapproved()
    serializer_class = serializers.GalleryPrivateSerializer
    http_method_names = ['get', 'delete']
    permission_classes = [permissions.IsAuthenticated]


class GalleryApproveViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.notapproved()
    serializer_class = serializers.GalleryApproveSerializer
    http_method_names = ['patch', ]
    permission_classes = [permissions.IsAuthenticated]
