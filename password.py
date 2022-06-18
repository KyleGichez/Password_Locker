class User:
    """Initialize credentials instances"""
    user_accounts = dict()
    def __init__(self, first_name, last_name, username, password):
        """Initialize user class instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.credentials = dict()
    
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
    
    def addCredential(self, credential):
        """Add a new user credential"""
        self.credentials.update({
            credential.site : {
                'username' : credential.username,
                'password' : credential.password
            }
        })
    
    def deleteCredential(self, credential):
        """Delete an existing user credential"""
        self.credentials.clear({
            credential.site : {
                'username' : credential.username,
                'password' : credential.password
            }
        })

    def viewCredentials(self, credential):
        """View all credentials"""
        for credential in self.credentials:
            return credential


class Credentials:
    """Initialize user instances"""
    def __init__(self, site, username, password):
        self.site = site
        self.username = username
        self.password = password
    
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
        Password = input(new_password)
        return Password
