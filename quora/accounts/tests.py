from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    def test_create_user(self):
        User=get_user_model()
        user=User.objects.create(
            username='sanix',
            email='sanicksikani@gmail.com',
            password='19972017Russia',
            date_of_birth='1997-02-08'
        )
        self.assertEqual(user.username, 'sanix')
        self.assertEqual(user.email, 'sanicksikani@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User=get_user_model()
        admin_user=User.objects.create_superuser(
            username='superadmin',
            email='superadmin@gmail.com',
            password='19972017',
            date_of_birth='1997-08-02'
        )    
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_admin)

