import unittest
from password import (
    Credentials, User
)

class TestUser(unittest.TestCase):
    def setUp(self):
        """create a new user account"""
        self.new_user_account = User("Twitter")

    def test_init(self):
        """test initialization of new user account"""
        self.assertEqual(self.new_user_account.acc1, "Twitter")


if __name__ == '__main__':
    unittest.main()