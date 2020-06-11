from celery import shared_task
from PIL import Image
@shared_task
def update_image(path, width, heigth):
    image = Image.open(path)
    output_size = (width, heigth)
    image.thumbnail(output_size)
    image.save(path)
    return output_size
