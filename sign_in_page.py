#Shows what the user can have access to when they sign in

from account import Account
from search_image import Search_Image
import json

class Sign_In_Page:
    
    def __init__(self, account, Acc_list):
        self.account = account
        self.accountList = Acc_list
        # self.options = {

        #     "1": self.search_photo,

        #     "2": self.show_gallery,

        #     "3": self.change_username,

        #     "4": self.change_email,

        #     "5": self.change_password,

        #     "6": self.delete_account
        # }

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

    def display_options(self):  
        print(f""" 
             Hi {self.account.username}, you've successfully signed in! 
             Please choose one of the options below:
 
             1. Search Photos
             2. Show Gallery
             3. Change Username
             4. Change email address
             5. Change password
             6. Delete account
             Q. Sign Out
             """)

    def search_photo(self, search):
        image = Search_Image(search)
        return image.image_links
        
    
    # def show_gallery(self):
    #     for key, value in self.account.gallery.items():
    #         print(key, ' : ', value)
    #     return True

    def update_account(self, new_username, new_password, new_email):
        for acc in self.accountList:
            if acc.username == new_username:
                return True
        else:
            self.account.username = new_username
            self.account.password = new_password
            self.account.email = new_email
            return False

    # def change_username(self):
    #     new_username = str(input('Enter the new username: '))
    #     self.account.username = new_username
    #     print(f"Your username has been changed to \"{new_username}\"\n")
    #     self.save()
    #     return True

    # def change_email(self):
    #     new_email = str(input('Enter the new email: '))
    #     self.account.email = new_email
    #     print(f"Your email has been changed to \"{new_email}\"\n")
    #     self.save()
    #     return True
        
    # def change_password(self):
    #     new_password = str(input('Enter the new password: '))
    #     self.account.password = new_password
    #     print(f"Your password has been changed to \"{new_password}\"\n")
    #     self.save()
    #     return True

    def delete_account(self, password):
        for i in range(len(self.accountList)):
            if self.accountList[i].username == self.account.username:
                pop_acc = self.accountList[i]
                if password == pop_acc.password:
                    self.accountList.pop(i)
                    return False
                else:
                    return True
           


        # for i in range(len(self.accountList)):
        #     if self.accountList[i].username == self.account.username:
        #         pop_acc = self.accountList[i]
        #         #password = input("Please enter the account's password for confirmation: ")
        #         if password == pop_acc.password:
        #             self.accountList.pop(i)
        #             print(f"Your account \'{self.account.username}\' has been successfully deleted!")
        #             self.save()
        #             return False
        #         else:
        #             print("The password is invalid, please try again.")
        # return True        

    def run(self):
        while True:
            #self.display_options()  
            option = input("Enter an option: ")
            if option.lower() == "q":
                break

            action = self.options.get(option)
            if action:
                return_statement = action()
                if return_statement == False:
                    break
            else:
                print("{0} is not a valid option, please try again!".format(option))
