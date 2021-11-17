from datetime import datetime
from rest_framework import serializers
from gallery.models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['image', 'image_thumb']


class GalleryPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'image', 'image_thumb', 'created_at', 'created_at_strftime']


class GalleryApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['approved_at']

    def update(self, instance, validated_data):
        instance.approved_at = datetime.now()
        instance.save()

        return instance
