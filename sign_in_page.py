#Shows what the user can have access to when they sign in

from account import Account
from search_image import Search_Image
import json

class Sign_In_Page:
    
    def __init__(self, account, account_list):
        self.account = account
        self.account_list = account_list

    def save(self):
        with open("accounts.json", "w") as accounts_json:
            serilizated_data = self.serilization()
            json.dump(serilizated_data, accounts_json,sort_keys=True, indent=4)
    
    def serilization(self):
        exeList=[]
        for i in range(len(self.accountList)):
            serilizated = {}
            serilizated["username"] = self.accountList[i].username
            serilizated["password"] = self.accountList[i].password
            serilizated["email"] = self.accountList[i].email
            serilizated["gallery"] = self.accountList[i].gallery
            exeList.append(serilizated)
        return exeList

    def search_photo(self, search):
        image = Search_Image(search)
        return image.image_links

    def update_account(self, old_username, old_password, old_email, new_username, new_password, new_email):

        for acc in self.account_list:
            if (acc.username == new_username and self.account.username != new_username) or (acc.email == new_email and self.account.email != new_email):
                return (True, None)
        else:
            
            self.account.username = new_username
            self.account.password = new_password
            self.account.email = new_email
            return (False, self.account)

    def delete_account(self):
        for i in range(len(self.account_list)):
            if self.account_list[i].username == self.account.username:
               self.account_list.pop(i)
               return True
        else:
            return False

    # def run(self):
    #     while True:  
    #         option = input("Enter an option: ")
    #         if option.lower() == "q":
    #             break

    #         action = self.options.get(option)
    #         if action:
    #             return_statement = action()
    #             if return_statement == False:
    #                 break
    #         else:
    #             print("{0} is not a valid option, please try again!".format(option))
