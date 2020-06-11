from django.test import TestCase
from .tasks import update_image
from .models import Content

class URLTest(TestCase):
    def setUp(self):
        pass
    def test_main_page(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_rest_page(self):
        resp = self.client.get('/rest/')
        self.assertEqual(resp.status_code, 200)

    def test_task_page_single_object(self):
        for i in range(5):
            resp = self.client.get('/task/{}/'.format(i))
            self.assertEqual(resp.status_code, 200)

# class TaskTest(TestCase):
#     def test_scale_image(self):
#         path = Content.objects.get(id=4).image.path
#         output_size = update_image(path,500, 500) 
#         self.assertEqual(output_size, (500,500))

    

