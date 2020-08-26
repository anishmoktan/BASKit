# The back-bone of the application
# Will have the CRUD for accounts and a Sign-in option
# Need to connect to the API
import json
from account import Account
from sign_in_page import Sign_In_Page


class Application:
    def __init__(self, accountDic=[]):
        self.accountDict = accountDic

    def sign_up(self,username,password,email):
        #username = input("Please enter a username for your account: ")
        for acc in self.accountDict:
            if acc.username == username:
                return(
                    f"An account with the username and/or email {username} {email} already exists, please try again!")
                
        else:
            #password = input("Please enter a password: ")
            #email = input("Please enter an email address: ")
            account = Account(username, password, email)
            self.accountDict.append(account)
            return(
                f"Congratulations, you've successfully created an account with the username \"{username}\"!")

    def sign_in(self):
        if self.accountDict == []:
            print("There are no accounts in the application to sign in to!\n")
        else:
            username = str(input("Please enter your username to sign in: "))
            for acc in self.accountDict:
                    if acc.username == username:
                        account_info = acc
                        password = str(input("Please enter your password: "))
                        if password == account_info.password:
                            sign_In = Sign_In_Page(account_info,self.accountDict)
                            sign_In.run()
                            break
                        else:
                            print("Wrong password, please try again!")
                            break
            else:
                print(f'The username \"{username}\" does not exist in our system!')
                 
    @classmethod
    def from_json(cls, data):
        # data is the accounts from the accounts.json
        decoded_accounts = []
        for i in range(len(data)):
            decoded_accounts.append(Account.from_json(data[i]))
        return decoded_accounts

    def load(self):
        with open("accounts.json", "r") as accounts_json:
            data = json.load(accounts_json)
            decoded_accounts = Application.from_json(data)
            self.accountDict = decoded_accounts

    def save(self):
        with open("accounts.json", "w") as accounts_json:
            serilizated_data = self.serilization()
            json.dump(serilizated_data, accounts_json,sort_keys=True, indent=4)

    def serilization(self):
        exeList=[]
        for i in range(len(self.accountDict)):
            serilizated = {}
            serilizated["username"] = self.accountDict[i].username
            serilizated["password"] = self.accountDict[i].password
            serilizated["email"] = self.accountDict[i].email
            serilizated["gallery"] = self.accountDict[i].gallery
            exeList.append(serilizated)
        return exeList
