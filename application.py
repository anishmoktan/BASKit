import json
from account import Account
from sign_in_page import Sign_In_Page

class Application:
    def __init__(self, accountDic=[]):
        self.accountDict = accountDic
        
    def sign_up(self,username,password,email):
        for acc in self.accountDict:
            if acc.username == username:
                return True
        else:
            account = Account(username, password, email)
            self.accountDict.append(account)
            return False

    def sign_in(self, username, password):
        if self.accountDict == []:
            return (True,None)
        else:
            for acc in self.accountDict:
                if acc.username == username and acc.password == password:
                    return (False, acc)
            else:
                return (True, None)

    @classmethod
    def from_json(cls, data):
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
        exeList = []
        for i in range(len(self.accountDict)):
            serilizated = {}
            serilizated["username"] = self.accountDict[i].username
            serilizated["password"] = self.accountDict[i].password
            serilizated["email"] = self.accountDict[i].email
            serilizated["gallery"] = self.accountDict[i].gallery
            exeList.append(serilizated)
        return exeList
