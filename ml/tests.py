from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_scan_view(self):

        existing_photo_path = "./media/test-photo.png"
        with open(existing_photo_path, "rb") as file:
            image_file = SimpleUploadedFile("test-photo.png", file.read())

        # Make a POST request to the scan view with the test image file
        response = self.client.post(reverse("scan"), {"image": image_file})

        # Assert that the response has a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the expected template is used for rendering the response
        self.assertTemplateUsed(response, "result-retin.html")

        # Clean up the created test image file
        image_file.close()




    def test_result_view(self):
        # Prepare the data for the POST request
        data = {
            'quantity': 5.0,
            'cho0': 1,
            'cho': 1,
            'cho1': 1,
            'cho2': 1,
            'cho3': 0,
            'cho4': 1,
            'cho5': 0,
            'cho6': 1,
            'cho7': 1,
            'cho8': 0,
            'cho9': 1,
            'cho11': 1,
            'cho12': 0,
            'cho13': 1,
            'cho14': 1,
        }

        # Make a POST request to the result view
        response = self.client.post(reverse('early-result'), data)

        # Assert the response status code and template used
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'result-early-diagnosis.html')


    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')



    def test_earlydiagnosis_view(self):
        response = self.client.get('/early-diagnosis/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'early-diagnosis.html')



    def test_signup_view_get(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign-up.html')

    def test_signup_view_post(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        }
        response = self.client.post(reverse('signup'), data)
        self.assertRedirects(response, reverse('signin'))

    def test_signup_view_existing_username(self):
        data = {
            'username': 'testuser',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        }
        response = self.client.post(reverse('signup'), data)
        self.assertTemplateUsed(response, 'sign-up.html')
        self.assertContains(response, 'Username already exists.')

    def test_signup_view_existing_email(self):
        data = {
            'username': 'newuser',
            'email': 'testuser@example.com',
            'password': 'newpassword'
        }
        response = self.client.post(reverse('signup'), data)
        self.assertTemplateUsed(response, 'sign-up.html')
        self.assertContains(response, 'Email already exists.')

    def test_signin_view_get(self):
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign-in.html')

    def test_signin_view_post_success(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertRedirects(response, '/')

    def test_signin_view_post_invalid_credentials(self):
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertTemplateUsed(response, 'sign-in.html')
        self.assertContains(response, 'Invalid username or password')

    def test_logoutuser_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/')

    def test_faqs_view(self):
        response = self.client.get(reverse('faqs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs.html')

    def test_foodpoints_view(self):
        response = self.client.get(reverse('foodpoints'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food-points.html')

    def test_steps_view(self):
        response = self.client.get(reverse('steps'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'steps.html')

    def test_chatbot_view(self):
        response = self.client.get(reverse('chatbot'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chatbot.html')
