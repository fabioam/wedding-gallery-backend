from django.db import models
from sorl.thumbnail import ImageField as SorlImageField, get_thumbnail
from gallery.manager import GalleryManager


class Gallery(models.Model):
    image = SorlImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    objects = GalleryManager()

    @property
    def image_thumb(self):
        if not self.image:
            return None

        image = get_thumbnail(self.image, '300x300', quality=90)
        return image.url

    @property
    def created_at_strftime(self):
        return self.created_at.strftime('%d/%m/%Y %H:%M')
