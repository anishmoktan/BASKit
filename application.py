#The back-bone of the application
#Will have the CRUD for accounts and a Sign-in option
#Need to connect to the API

class Application:
    def __init__(self, accountDic={}):
        self.accountDict = accountDic
    def sign_up(self):
        username= input("Please enter the username: ")
        if username not in self.accountDict.keys():
            account = Account(username)
            self.accountDict[username] = account
            print(f"Congratulations, you've successfully created an account with the username \"{username}\"!")
        else:
            print(f"An account with the username \"{username}\" already exists, please try again!")
    def search_account(self):
        if self.accountDict= {}:
            print("There are currenlty no accounts to look up in our system")
    def delete_account(self):
        if self.accountDict={}:
            print("There are currently no accounts to delete in our system")
    