from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class CreateUserTestCase(TestCase):
    """ Testing UserRegistrationView """

    valid_data = {
        'first_name': 'first',
        'last_name': 'second',
        'middle_name': 'middle',
        'date_birth': '2000-01-01',
        'username': 'test',
        'password': '1234',
        'password_again': '1234'
    }

    def setUp(self):
        self.client = Client()

    def test_status_code(self):
        """ Test status code """
        response = self.client.post(reverse('user_profile:create_user'), self.valid_data)

        self.assertEqual(response.status_code, 302)

    def test_create_user(self):
        """ Test successful registration """
        self.client.post(reverse('user_profile:create_user'), self.valid_data)

        user = get_user_model().objects.last()

        self.assertEqual(user.first_name, self.valid_data['first_name'])
        self.assertEqual(user.last_name, self.valid_data['last_name'])
        self.assertEqual(user.middle_name, self.valid_data['middle_name'])
        self.assertEqual(user.date_birth.strftime('%Y-%m-%d'), self.valid_data['date_birth'])
        self.assertEqual(user.username, self.valid_data['username'])

    def test_invalid_data(self):
        """ Test in case when data is invalid (user isn't create) """
        invalid_data = {
            'first_name': 'first',
            'last_name': 'second',
            'middle_name': 'middle',
            'date_birth': 'qwerty',  # it's wrong
            'username': 'test',
            'password': '1234',
            'password_again': '1234'
        }
        response = self.client.post(reverse('user_profile:create_user'), invalid_data)

        self.assertEqual(response.status_code, 200)

    def test_not_equal_passwords(self):
        """ Test in case when password != password_again (user isn't create) """
        invalid_data = {
            'first_name': 'first',
            'last_name': 'second',
            'middle_name': 'middle',
            'date_birth': 'qwerty',  # it's wrong
            'username': 'test',
            'password': '1234',
            'password_again': '4321'
        }
        response = self.client.post(reverse('user_profile:create_user'), invalid_data)

        self.assertEqual(response.status_code, 200)
