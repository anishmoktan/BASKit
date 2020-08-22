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

            "4": self.account.display_s,

            "5": self.account.checkout
        }

    def display_options(self):
        print(""" 
             You have successfully signed in! 
             Please choose one of the options below:
 
             1. Search Photos
             2. Update Account
             3. Show Gallery
             Q. Sign Out
             """)

   
    def run(self):
        while True:
            self.display_options()
            self.order_menu()

            option = input("Enter an option: ")

            if option.lower() == "q":
                break

            action = self.options.get(option)
            if action:
                action()

            else:
                print(
                    "{0} is not a valid option, Please try again".format(option))

    def search_photo(self):

        try:
            amount = float(
                input("Enter the amount of money you want to add: "))

            if amount < 0:
                raise Exception("Cannot accept negative value")

            self.account.add_balance(amount)

        except Exception as NegativeAmountError:
            print(NegativeAmountError)

        except:
            print("Only number is allowed!")

    def update_account(self):

        item_name = input("Enter the name of the item: ").lower()

        if item_name in self.price.keys():

            try:
                item_amount = int(
                    input(f"How many of {item_name} do you want: "))

                item_total_price = self.price[item_name] * item_amount

                self.account.add_to_shopping_cart(
                    (item_name, item_amount, item_total_price))

            except ValueError:
                print("Only number is allowed!")

        else:
            print(f"\"{item_name}\" not in the list")

        time.sleep(2)

    def show_gallery(self):

        if len(self.account.shopping_cart) > 0:

            target_name = input("Enter the name of the item: ").lower()
            if target_name in self.price.keys():
                self.account.remove_from_shopping_cart(target_name)
            else:
                print(f"\"{target_name}\" not in the list")
        else:
            print("You don't have anything in your shopping cart")

        time.sleep(2)