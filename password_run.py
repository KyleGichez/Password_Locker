from password import(
    User, Credentials
)

def main():
    current_user = None
    while True:
        print("Use the short code: cc - create account, ll - login")
        short_code = input("What would you  like to do? > ").lower()
        if short_code == "cc":
            first_name = input("First Name\t> ")
            last_name = input("Last Name\t> ")
            username = input("Username\t> ")
            passcode = input("Password\t> ")
            user = User(first_name, last_name, username, passcode)
            user.save()
            print(f"New user account {first_name} {last_name} successfully created.")
            pass
        elif short_code == "ll":
            main_username = input("Enter username > ")
            password = input("Enter password > ")
            user = User.getByUserName(main_username)
            current_user = user if user.checkPasswordMatch(password) else None
            print(f"Hello {current_user.first_name} how are you doing today, What would you like to do with your password locker?")
            break
        else:
            print("You entered an invalid short code, please try again.")
            pass

    while current_user:
        print()
        print("Use these short codes ls-list all accounts, fc-find account, dl-delete account, ac-add credential, lsc-list all credentials, dlc-delete credential, ex-exit")
        print()
        short_code = input('> ').lower()
        if short_code == 'ls':
            accounts = current_user.listUserAccounts()
            index = 1
            for account in accounts:
                print(f'{index}. Username : {account[0]} \n First Name : {account[1].first_name} \n Last Name : {account[1].last_name} ')
                index += 1

        elif short_code == 'fc':
            username = input("Enter the username you want to search for > ")
            account = current_user.getByUserName(username)
            # print(account, dir(account), type(account))
            if account:
                print(f"First Name: {account.first_name} \n Last Name: {account.last_name}")
            else:
                print(f"Oops, that user account is not available.")

        elif short_code == 'dl':
            username = input("Enter the username you want to delete > ")
            account = current_user.deleteUser(username)
            
        elif short_code == 'ac':
            site = input("Enter website name\t> ")
            credential_username = input(f"Enter username for {site}\t> ")
            passcode = input("Enter password here\t> ")
            credential = Credentials(site, credential_username, passcode)
            current_user.addCredential(credential)
            print(f"New user credential {site} successfully created.")

        elif short_code == 'lsc':
            credentials = current_user.listCredentials()
            index = 1  
            for credential in credentials:
                print(f"{index}. {credential}")
                index += 1

        elif short_code == 'dlc':
            website = input("Enter the website name you want to delete > ")
            credential = current_user.deleteCredential(website)
            
        else:
            if short_code == 'ex':
                print("Bye, enjoy your day honey!")
                break


if __name__ == '__main__':
    main()