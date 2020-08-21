#Will have the class for each accounts
class Account():
    def __init__(self, username):
        self.username = username
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
    
    def search_image():

    def view_image():
    
    def update_account():
    
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


