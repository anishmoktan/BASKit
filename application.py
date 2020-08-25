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
        if self.accountDict == []:
            print("There are no accounts to delete!\n")
        else:
            username = input("Please enter the username you're deleting: ")
            for acc in range(len(self.accountDict)-1):
                if self.accountDict[acc].username == username:
                    account_info = self.accountDict[acc]
                    password = input("Please enter the account's password for confirmation: ")
                    if password == account_info.password:
                        self.accountDict.pop(acc)
                    else:
                        print("The password is invalid, please try again.")
                        break
                else:
                    print(f'The username you\'ve entered, \"{username}\", does not exist. Please try again!')

    def sign_in(self):
        if self.accountDict == []:
            print("There are no accounts in the application to sign in to!\n")
        else:
            username = str(input("Please enter your username to sign in: "))
            for acc in self.accountDict:
                try:
                    if acc.username == username:
                        account_info = acc
                        password = str(input("Please enter your password: "))
                        if password == account_info.password:
                            sign_In = Sign_In_Page(account_info)
                            sign_In.run()
                            break
                        else:
                            print("Wrong password, please try again!")
                finally :
                    print(f'{username} does not exist in our system, please try again!')
                    return sign_in
    
    


            # for acc in range(len(self.accountDict)-1):
            #     if self.accountDict[acc].username == username:
            #         account_info = self.accountDict[acc]
            #         password = str(input("Please enter your password: "))
            #         if password == account_info.password:
            #             sign_In = Sign_In_Page(account_info)
            #             sign_In.run()
            #         else:
            #             print("Wrong password, please try again!")
            #     else:
            #         print(f'The username you enetered, \"{username}\", does not exist. Please try again')
            
            # for acc in range(len(self.accountDict)-1):
            #     if self.accountDict[acc].username == username:
            #         account_info = self.accountDict[acc]
            #         password = str(input("Please enter your password: "))
            #         if password == account_info.password:
            #             sign_In = Sign_In_Page(account_info)
            #             sign_In.run()
            #         else:
            #             print("Wrong password, please try again!")
            #     else:
            #         print(f'The username you enetered, \"{username}\", does not exist. Please try again')


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
