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

    def checkPasswordMatch(self, password):
        if password == self.password:
            return True
        else:
            return False

    def save(self):
        """Save user account"""
        self.user_accounts[self.username] = self
        return self or None
    
    @classmethod
    def getByUserName(cls, username):
        """Get user by username"""
        account = cls.user_accounts.get(username)
        return account
    
    @classmethod
    def listUserAccounts(cls):
        """View all user accounts"""
        return cls.user_accounts.items()

    def addCredential(self, credential):
        """Add a new user credential"""
        self.user_credentials[credential.site] = {
            'username' : credential.username,
            'password' : credential.password
        }
        return self.user_credentials.get(credential.site)

    def deleteCredential(self, site_name):
        """Delete an existing credential"""
        self.user_credentials.pop(site_name)
        return True

    def listCredentials(self):
        """List all user credentials"""
        return [f"Your {credential[0]} username is {credential[1].get('username')}." for credential in self.user_credentials.items() if credential]

    @classmethod
    def deleteUser(cls, username):
        """Delete an existing user account"""
        cls.user_accounts.pop(username)
        return True


class Credentials:
    """Initialize user instances"""
    def __init__(self, site, username, password):
        self.site = site
        self.username = username
        self.password = password

    def save(self):
        self.site = {
            'username' : self.username,
            'password' : self.password
        }

    def createRandomPassword(self, length=10):
        """create a random password"""
        import random
        import string
        password_letters = string.ascii_lowercase
        random_password = ''.join(random.choice(password_letters) for i in range(length))
        self.password = random_password
        return self.password

    def createNewPassword(self, new_password):
        """Create a new password"""
        self.password = new_password
        return True

