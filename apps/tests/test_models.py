from django.test import TestCase
from apps.users.models import User

class SimpleTest(TestCase):
	def test_create_user(self):
		user=User.objects.create_user(username='test',email='test@test.com')
		user.save()
		self.assertEqual(user.username,'test')
