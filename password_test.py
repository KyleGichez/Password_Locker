import unittest
from password import (
    Credentials, User
)

class TestUser(unittest.TestCase):
    def setUp(self):
        """Create a new user account"""
        users = dict()
        self.user1 = User("Aklisiya", "Eshetu", "beautifulaklisiya", "sweetbabyboo")


    def test_init(self):
        """Test init user account credentials"""
        self.assertEqual(self.user1.first_name, "Aklisiya")
        self.assertEqual(self.user1.last_name, "Eshetu")
        self.assertEqual(self.user1.username, "beautifulaklisiya")
        self.assertEqual(self.user1.password, "sweetbabyboo")

    def test_add_user(self):
        """Test add a new user account"""
        self.user1 = User("Aklisiya", "Eshetu", "beautifulaklisiya", "sweetbabyboo")
        self.user1.save()
        self.user2 = User("Sexy Ms", "Dollar Baby", "sexymsdollarbaby", "Sexyoungdon")
        self.user2.save()

    def test_save(self):
        """Test save new user account"""
        self.user1 = User("Aklisiya", "Eshetu", "beautifulaklisiya", "sweetbabyboo")
        self.user1.save()

    def test_view_accounts(self):
        """Test view user accounts"""
        self.user1 = User("Aklisiya", "Eshetu", "beautifulaklisiya", "sweetbabyboo")
        self.user1.save()
        self.user1.viewUserAccounts()

    def test_delete(self):
        """Test delete an existing user account"""
        self.user1 = User("Aklisiya", "Eshetu", "beautifulaklisiya", "sweetbabyboo")
        self.user1.save()
        self.user1.deleteUser()

class TestCredentials(unittest.TestCase):
    def setUp(self):
        """Create a new user credential"""
        self.user1 = Credentials("Twitter", "aklisiyababy", "eshetuhabesha")

if __name__ == '__main__':
    unittest.main()