def main():
    username = input("Enter username: ")
    print(f"Hello {username}, welcome back, how are you doing today?")

    while True:
        print("What would you like to do with your password locker today?.")
        print("Use these short codes cc-create a user account, ls-list all user accounts, fc-find user account, dc-delete user account, ac-add user credential, lsc-list all user credentials, dc-delete user credential")
        print()
if __name__ == '__main__':
    main()