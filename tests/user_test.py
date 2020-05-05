# import unittest
# from app.models import User

# class test_userModel(unittest.TestCase):
#     # to test behaivours in the user model

# def setUp(self):
#     self.new_user = User(password='mypassword')

# def test_setPassword(self):
#     # to test if there is a password
#     self.assertTrue(self.new_user.secure_pass is not None)

# def test_check_password(self):
#     self.assertTrue(self.new_user.check_password('mypassword'))


import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))