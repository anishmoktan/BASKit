#Shows what the user can have access to when they sign in

from account import Account
from search_image import Search_Image
import json
import requests
import os

class Sign_In_Page:
    
    def __init__(self, account):
        self.account = account
        self.options = {

            "1": self.search_photo,

            "2": self.update_account,

            "3": self.show_gallery,
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
        ans= input("Would you like to save the image to your gallary?").lower()
        print("Please enter either yes or no")
        if ans== 'yes':
            self.account.gallery[counter]=image.image_link
            self.counter += 1
        else:
            return display_options

    
    def show_gallery(self):
        for key, value in self.account.gallery.items():
            print(key, ' : ', value)

    def change_username(self):
        new_username= str(input('Enter the new username: '))
        self.account.username=new_username

    def change_email(self):
        new_email= str(input('Enter the new email: '))
        self.account.email=new_email
        

        

    def show_gallery(self):

        if len(self.account.shopping_cart) > 0:

            target_name = input("Enter the name of the item: ").lower()
            if target_name in self.price.keys():
                self.account.remove_from_shopping_cart(target_name)
            else:
                print(f"\"{target_name}\" not in the list")
        else:
            print("You don't have anything in your shopping cart")

    

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
                print(
                    "{0} is not a valid option, Please try again".format(option))
