from django.test import TestCase
from .models import CustomUser

class UserModelTest(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(username='test', password='12345')
        self.assertEqual(user.username, 'test')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

