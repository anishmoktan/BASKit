#Shows what the user can have access to when they sign in

from account import Account
from search_image import Search_Image
import json

class Sign_In_Page:
    
    def __init__(self, account, Acc_list):
        self.account = account
        self.accountList = Acc_list
        self.options = {

            "1": self.search_photo,

            "2": self.show_gallery,

            "3": self.change_username,

            "4": self.change_email,

            "5": self.change_password,

            "6": self.delete_account
        }

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

    def search_photo(self):
        search = input('What image would you like to search?: ')
        image = Search_Image(search)
        ans = str(input("Would you like to save the image to your gallary? (yes/no): ").lower())
        if ans == 'yes':
            self.account.gallery[search]=image.image_link
        else:
            return True
    
    def show_gallery(self):
        for key, value in self.account.gallery.items():
            print(key, ' : ', value)
        return True

    def change_username(self):
        new_username = str(input('Enter the new username: '))
        self.account.username = new_username
        print(f"Your username has been changed to \"{new_username}\"\n")
        return True

    def change_email(self):
        new_email = str(input('Enter the new email: '))
        self.account.email = new_email
        print(f"Your email has been changed to \"{new_email}\"\n")
        return True
        
    def change_password(self):
        new_password = str(input('Enter the new password: '))
        self.account.password = new_password
        print(f"Your password has been changed to \"{new_password}\"\n")
        return True

    def delete_account(self):
        for i in range(len(self.accountList)):
            if self.accountList[i].username == self.account.username:
                pop_acc = self.accountList[i]
                password = input("Please enter the account's password for confirmation: ")
                if password == pop_acc.password:
                    self.accountList.pop(i)
                    print(f"Your account \'{self.account.username}\' has been successfully deleted!")
                    return False
                else:
                    print("The password is invalid, please try again.")
        return True        

    def run(self):
        while True:
            self.display_options()  
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
