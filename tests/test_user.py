import unittest
from app.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username = 'njiiri',email='njerinjiiri@gmail.com,bio=Bio should read coding',password='Jamlick12')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_password_access(self):
        with self.assertTrue(AttributeError):
            self.new_user.password_hash

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('Jamlick12'))
