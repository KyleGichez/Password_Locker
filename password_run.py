from password import(
    User,Credentials
)
def main():
    main_username = input("Enter username: ")
    print(f"Hello {main_username} welcome back, how are you doing today? What would you like to do with your password locker today?")

    while True:
        print()
        print("Use these short codes cc-create a user account, ls-list all user accounts, fc-find user account, dc-delete user account, ac-add user credential, lsc-list all user credentials, dc-delete user credential")
        print()

        short_code = input().lower()

        if short_code == 'cc':
            first_name = input("First Name:.......")
            last_name = input("Last Name:.......")
            username = input("Username:.......")
            password = input("Password:.......")

            User.save(User.addUser(first_name, last_name, username, password))
            print(f"New contact {first_name} {last_name} successfully created.")
            print()


if __name__ == '__main__':
    main()