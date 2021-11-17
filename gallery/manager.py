from django.db import models


class GalleryManager(models.Manager):
    def approved(self):
        return self.get_queryset().filter(approved_at__isnull=False).order_by('-approved_at')

    def notapproved(self):
        return self.get_queryset().filter(approved_at__isnull=True).order_by('created_at')