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
    
    def addUser(self):
        """Add a new user account"""
        self.user_credentials.update({
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'username' : self.username,
            'password' : self.password
        })

    def save(self):
        """Save user account"""
        self.user_accounts[self.username] = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password
        }
        return self
    
    def getByUserName(self, username):
        """Get user by username"""
        return self.user_accounts.get(username)

    def viewUserAccounts(self):
        """View all user accounts"""
        for self.user_credentials in self.user_accounts:
            return self.user_credentials
    
    def deleteUser(self):
        """Delete an existing user account"""
        self.user_credentials.clear()


class Credentials:
    """Initialize user instances"""
    def __init__(self, site, username, password):
        self.site = site
        self.username = username
        self.password = password
        self.credentials = dict()
    
    def createRandomPassword(self, length):
        self.length = length
        """create a random password"""
        import random
        import string
        password_letters = string.ascii_lowercase
        random_password = ''.join(random.choice(password_letters) for i in range(self.length))
        return random_password

    def createNewPassword(self, new_password):
        """Create a new password"""
        new_password = input("Enter new password:")
        return new_password

    def addCredential(self, credential):
        """Add a new user credential"""
        self.credentials.update({
            credential.site : {
                'username' : credential.username,
                'password' : credential.password
            }
        })

    def deleteCredential(self, credential):
        """Delete an existing credential"""
        self.credentials.clear({
            credential.site : {
                'username' : self.username,
                'password' : self.password
            }
        })
