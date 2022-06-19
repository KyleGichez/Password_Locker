import unittest
from password import (
    Credentials, User
)

class TestUser(unittest.TestCase):
    def setUp(self):
        """Create a new user account"""
        self.user1 = User("Aklisiya", "Eshetu", "beautifulaklisiya", "sweetbabyboo")
        results = self.user1.save()
        self.assertTrue(results)

    def test_init(self):
        """Test initialize user account credentials"""
        self.assertEqual(self.user1.first_name, "Aklisiya")
        self.assertEqual(self.user1.last_name, "Eshetu")
        self.assertEqual(self.user1.username, "beautifulaklisiya")
        self.assertEqual(self.user1.password, "sweetbabyboo")

    # def test_saveUser(self):
    #     """Test add a new user account"""
        
    def tearDown(self):
        """tearDown method"""
        self.user1.user_accounts = dict()

    def test_viewAccounts(self):
        """Test view all user accounts"""
        accounts = self.user1.listUserAccounts()
        self.assertEqual(len(accounts), 1)

    def test_getUser(self):
        """Test get a user account by username"""
        account = self.user1.getByUserName("beautifulaklisiya")
        self.assertEqual(self.user1.username, "beautifulaklisiya")
        return account

    def test_addCredential(self):
        """Test save a new credential"""
        credential_1 = Credentials("Tiktok", "eshetubabyhabesha", "sexybaby")
        self.user1.addCredential(credential_1)
        self.assertEqual(len(self.user1.user_credentials.items()), 1)

    def test_deleteCredential(self):
        """Test delete an existing credential"""
        credential_1 = Credentials("Tiktok", "eshetubabyhabesha", "sexybaby")
        self.user1.addCredential(credential_1)
        self.user1.deleteCredential("Tiktok")
        self.assertEqual(len(self.user1.user_credentials.items()), 0)

    def test_delete(self):
        """Test delete an existing user account"""
        self.user1.deleteUser("beautifulaklisiya")
        self.assertEqual(len(self.user1.user_accounts), 0)


class TestCredentials(unittest.TestCase):
    def setUp(self):
        """Create a new user credential"""
        self.user1 = Credentials("Tiktok", "aklisiyababy", "eshetuhabesha")

if __name__ == '__main__':
    unittest.main()