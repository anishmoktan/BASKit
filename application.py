# The back-bone of the application
# Will have the CRUD for accounts and a Sign-in option
# Need to connect to the API
import json
from account import Account
from sign_in_page import Sign_In_Page


class Application:
    def __init__(self, accountDic=[]):
        self.accountDict = accountDic

    def sign_up(self):
        username = input("Please enter a username for your account: ")
        for acc in self.accountDict:
            if acc.username == username:
                print(
                    f"An account with the username \"{username}\" already exists, please try again!")
                break

        else:
            password = input("Please enter a password: ")
            email = input("Please enter an email address: ")
            account = Account(username, password, email)
            self.accountDict.append(account)
            print(
                f"Congratulations, you've successfully created an account with the username \"{username}\"!")

    def delete_account(self):
        if self.accountDict == {}:
            print("There are no accounts to delete!\n")
        else:
            username = input("Please enter the username you're deleting: ")
            if username in self.accountDict.keys():
                self.accountDict.pop(username)
                print(
                    f"The account with username \"{username}\" has been successfully deleted!")
            else:
                print(
                    f"The account with username \"{username}\" does not exist!\n")

    def update_account(self):
        if self.accountDict == {}:
            print("There are no accounts in the application to update!\n")
        else:
            username = input("Please enter your username you're updating: ")
            if username in self.accountDict.keys():
                new_username = input(
                    "Please enter the new username for that account: ")
                update_account = self.accountDict[username]
                update_account.username = new_username
                self.accountDict[new_username] = self.accountDict.pop(username)
                print(
                    f"The username of \"{username}\" has been changed to \"{new_username}\"\n")
            else:
                print(
                    f"The account with username \"{username}\" does not exist!\n")

    def sign_in(self):
        if self.accountDict == {}:
            print("There are no accounts in the application to sign in to!\n")
        else:
            username = input("Please enter your username to sign in: ")
            if username in self.accountDict.keys():
                account_info = self.accountDict[username]
                password = str(input("Please enter your password: "))
                if password == account_info.password:
                    signed_In = Sign_In_Page(account_info)
                    signed_In.run()
                else:
                    print("Wrong password, please try again!")
            else:
                print(
                    f"The account with username \"{username}\" does not exist!\n")

    @classmethod
    def from_json(cls, data):

        # data is the accounts from the accounts.json
        decoded_accounts = {}
        for username, account in data.items():
            decoded_accounts[username] = Account.from_json(account)

        return decoded_accounts

    def load(self):
        with open("accounts.json", "r") as accounts_json:
            data = json.load(accounts_json)
            decoded_accounts = Application.from_json(data)
            self.accountDict = decoded_accounts

    def save(self):

        with open("accounts.json", "w") as accounts_json:
            serilizated_data = self.serilization()
            json.dump(serilizated_data, accounts_json,
                      sort_keys=True, indent=4)

    def serilization(self):
        serilizated = {}
        for username, account in self.accountDict.items():
            serilizated[username] = account.__dict__
        return serilizated
