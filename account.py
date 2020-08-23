import json


class Account():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.gallery={}
        self.counter=1
        self.options = {

            "1": self.search_image,

            "2": self.view_image,

            "3": self.update_account,
        }

    def display_options(self):
        print(""" 
            ************* BASKit version 1.0 *************
             You have successfully signed in! 
             Please choose one of the options below:
 
             1. Search an image
             2. View saved images
             3. Update username 
             Q. Sign out

             """)
    
    def search_image(self):
        search = input('What image would you like to search?')
        image = Search_Image(search)
        ans= input("Would you like to save the image to your gallary?").lower()
        print("Please enter either yes or no")
        if ans== 'yes':
            self.gallery[counter]=image.image_link
            self.counter += 1
        else:
            return display_options

    def view_image(self):
        print(self.gallery)
    
    def update_account(self):
        old_password = input('Please enter your old password: ')
        if old_password == self.password:
            new_password = input('Please enter a new password: ')
            self.password = new_password

        else:
            print("You have entered an invalid password!")

    
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
                print("{0} is not a valid option, Please try again".format(option))
    
    


