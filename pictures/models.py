from django.db import models
from pathlib import Path
from sorl.thumbnail import ImageField
from .tasks import update_image
import logging

logger = logging.getLogger(__name__)

class Content(models.Model):
    width = models.IntegerField()
    heigth = models.IntegerField()
    image = models.ImageField(blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            update_image.delay(self.image.path, self.width, self.heigth)
        except Exception as e:
            logger.error('Ошибка в таске: {}'.format(e))
