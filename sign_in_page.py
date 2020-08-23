#Shows what the user can have access to when they sign in

from account import Account
from search_image import Search_Image
import json
import requests
import os

class Sign_In_Page:
    
    def __init__(self, account):
        self.account = account
        self.app = Account
        self.options = {

            "1": self.search_photo,

            "2": self.show_gallery,

            "3": self.change_username,

            "4": self.change_email,

            "5": self.change_password,
        }

    def display_options(self):  
        print(""" 
             You have successfully signed in! 
             Please choose one of the options below:
 
             1. Search Photos
             2. Show Gallery
             3. Change Username
             4. Change email address
             5. Change password
             Q. Sign Out
             """)

    def search_photo(self):
        search = input('What image would you like to search?')
        image = Search_Image(search)
        ans= str(input("Would you like to save the image to your gallary?").lower())
        print("Please enter either yes or no")
        if ans== 'yes':
            self.account.gallery[search]=image.image_link
        else:
            return display_options
    
    def show_gallery(self):
        for key, value in self.account.gallery.items():
            print(key, ' : ', value)

    def change_username(self):
        new_username= str(input('Enter the new username: '))
    
        update_account = self.app.accountDict[self.account.username]
        update_account.username = new_username
        self.app.accountDict[new_username] = self.app.accountDict.pop(self.account.username)
        print(f"Your username has been changed to \"{new_username}\"\n")
        

    def change_email(self):
        new_email= str(input('Enter the new email: '))
        self.account.email=new_email
        
    def change_password(self):
        new_password= str(input('Enter the new password: '))
        self.account.password=new_password

    def run(self):
        while True:
            self.display_options()  
            option = input("Enter an option: ")
            if option.lower() == "q":
                break

            action = self.options.get(option)
            if action:
                action()
            else:
                print("{0} is not a valid option, please try again!".format(option))
