import tempfile
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GetProfileTestCase(APITestCase):
    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="noivos", is_staff=True, is_active=True)
        user.set_password('noivos123')
        user.save()

    def __temporary_image(self):
        """
        Generate and returns a temporary image file
        """
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file, 'jpeg')
        tmp_file.seek(0)  # important because after save(), the fp is already at the end of the file
        return tmp_file

    def test_workflow(self):
        data = {
            'image': self.__temporary_image(),
        }

        # upload a new picture
        url = reverse('gallery-list')
        response_upload = self.client.post(url, data, format='multipart')
        self.assertEqual(response_upload.status_code, status.HTTP_201_CREATED)

        # check if gallery still empty
        response_initial_gallery = self.client.get(reverse('gallery-list'))
        self.assertEqual(response_initial_gallery.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_initial_gallery.data), 0)  # should not contain any result yet

        # login as moderator (noivos)
        response_login = self.client.post(reverse('token_obtain_pair'), {
            'username': 'noivos',
            'password': 'noivos123'
        }, format='json')
        self.assertEqual(response_login.status_code, status.HTTP_200_OK)

        # set token to authenticated user
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response_login.data.get('access'))

        # get pending picture
        response_pending = self.client.get('/gallery/pending/')
        self.assertEqual(response_pending.status_code, status.HTTP_200_OK)

        # approve picture
        first_image = response_pending.data[0]
        response_approve = self.client.patch('/gallery/approve/%d/' % first_image.get('id'))
        self.assertEqual(response_approve.status_code, status.HTTP_200_OK)

        # count gallery again - it should have one picture now
        response_initial_gallery = self.client.get(reverse('gallery-list'))
        self.assertEqual(response_initial_gallery.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_initial_gallery.data), 1)  # should not contain any result yet


