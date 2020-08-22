#Will have the class for each accounts
<<<<<<< HEAD

import time
import json

class Account():
    def __init__(self, username, saved_images = []):
        self.username = username
        self.saved_images = saved_images

    def __str__(self):
        return(f"This is username: {self.username}"
                "This is your saved images: {self.saved_images}")


    @classmethod
    def from_json(cls, data):
        username, saved_images = data["username"], []
        for item in data["saved_images"]:
            tuple_item = tuple(item)
            saved_images.append(tuple_item)
        return cls(username=username,
                   saved_images=saved_images)


    def add_image(self, new_image):
        (new_image_name, new_image_count) = new_image
        for i in range(len(self.saved_images)):
            image = self.saved_images[i]
            (image_name, image_count) = image
            if image_name ==new_image_name:
                image_count += new_image_count
                self.saved_images.pop(i)
                self.saved_images.append((image_name, image_count))
                break
        else:
            self.saved_images.append(new_image)
        print(f"this is your all saved images: {self.saved_images}\n")



    def remove_image(self, target_image):
        for i in range(len(self.saved_images)):
            image = self.saved_images[i]
            image_name = image[0]
            if image_name == target_image:
                self.saved_images.pop(i)
                break
        else:
            print(f"\"{target_image}\" doesn't exist in your saved images.")
        print(f"this is your all saved images: {self.saved_images}\n")

        time.sleep(2)
=======
from search_image import Search_Image
from application import Application

class Account():
    def __init__(self, username, password,email):
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


>>>>>>> 9916f1036fb82afc602e902491cf7634c6171f5e
