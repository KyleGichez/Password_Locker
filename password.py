class User:
    """Initialize credentials instances"""
    user_accounts = dict()

    def __init__(self, first_name, last_name, username, password):
        """Initialize user class instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.user_credentials = dict()
    
    def save(self):
        """Save user account"""
        self.user_accounts[self.username] = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password
        }
        return True
    
    def getByUserName(self, username):
        """Get user by username"""
        return self.user_accounts.get(username)

    def listUserAccounts(self):
        """View all user accounts"""
        return self.user_accounts.items()

    def addCredential(self, credential):
        """Add a new user credential"""
        self.user_credentials.update({
            credential.site : {
                'username' : credential.username,
                'password' : credential.password
            }
        })
        return True

    def deleteCredential(self, site_name):
        """Delete an existing credential"""
        self.user_credentials.pop(site_name)
        return True
    
    def deleteUser(self, username):
        """Delete an existing user account"""
        self.user_accounts.pop(username)
        return True


class Credentials:
    """Initialize user instances"""
    def __init__(self, site, username, password):
        self.site = site
        self.username = username
        self.password = password
    
    def createRandomPassword(self, length=10):
        """create a random password"""
        import random
        import string
        password_letters = string.ascii_lowercase
        random_password = ''.join(random.choice(password_letters) for i in range(length))
        return random_password

    def createNewPassword(self, new_password):
        """Create a new password"""
        self.password = new_password
        return True

