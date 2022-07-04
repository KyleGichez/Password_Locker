from password import(
    User,Credentials
)
def main():
    main_username = input("Enter username > ")
    print(f"Hello {main_username} how are you doing today, What would you like to do with your password locker?")

    while True:
        print()
        print("Use these short codes cc-create account, ls-list all accounts, fc-find account, dc-delete account, ac-add credential, lsc-list all credentials, dc-delete credential, ex-exit")
        print()

        short_code = input().lower()

        if short_code == 'cc':
            first_name = input("First Name\t> ")
            last_name = input("Last Name\t> ")
            username = input("Username\t> ")
            passcode = input("Password\t> ")
            user = User(first_name, last_name, username, passcode)
            user.save()
            print(f"New user account {first_name} {last_name} successfully created.")
        
        elif short_code == 'ls':
            accounts = User.listUserAccounts()
            index = 1
            for account in accounts:
                print(f'{index}. Username : {account[0]} \n First Name : {account[1].get("first_name")} \n Last Name : {account[1].get("last_name")} ')
                index += 1

        elif short_code == 'fc':
            username = input("Enter the username you want to search for > ")
            account = User.getByUserName(username)
            # print(account, dir(account), type(account))
            if account:
                print(f"First Name: {account.get('first_name')} \n Last Name: {account.get('last_name')}")
            else:
                print(f"Oops, that user account is not available.")


if __name__ == '__main__':
    main()