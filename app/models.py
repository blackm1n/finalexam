from django.db import models
from django.utils.html import format_html
from django.conf import settings


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    steps = models.TextField()
    cook_time = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def image_tag(self):
        if self.image and self.image != 'False':
            return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(self.image.url))
        else:
            return ''

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True