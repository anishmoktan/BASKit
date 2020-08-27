from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin

from application import Application
from sign_in_page import Sign_In_Page

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/sign-up', methods=['POST'])
@ cross_origin()
def sign_up():
    data = request.get_json()
    username, password, email = data["username"], data["password"], data["email"]
    account_existed = project.sign_up(username, password, email)
    if account_existed:
        return {"message":"An account with the username and/or email already exists, please try again!"}, 400 #error
    else:
        project.save()
        return {"message":"Congratulations, you've successfully created an account"}, 200 #good

@app.route('/login', methods=['POST'])
@ cross_origin()
def login():
    data = request.get_json()
    username, password = data["username"], data["password"]
    account_existed , userdata = project.sign_in(username, password) 

    if account_existed:
        return {"message":"The username of the password you've entered in incorrect, please try again"}, 400 #error
    else:
        return {"message":"You've successfully signed in to your account", "data": userdata.__dict__ } , 200


@app.route('/search-photo', methods=['POST'])
@ cross_origin()
def search_photo():
    data = request.get_json()
    username, password, search_term = data["username"], data["password"], data["searchTerm"]
    account_existed , userdata = project.sign_in(username, password) 
    if account_existed:
        return {"message":"The username of the password you've entered in incorrect, please try again"}, 400 #error
    else:
        sign_In = Sign_In_Page(userdata,project.accountDict)
        search_result = sign_In.search_photo(search_term)
        if search_result:
            return {"message": "We found the photo you were looking for",
                    "photos": search_result
                    } , 200
        else:
            return {"message": "Did not find the photo you were looking for"}, 400

@app.route('/save-photo', methods=['POST'])
@ cross_origin()
def save_photo():
    data = request.get_json()
    username, password, photo_url = data["username"], data["password"], data["photoUrl"]
    account_existed , user_data = project.sign_in(username, password) 
    if account_existed:
        return {"message":"The username of the password you've entered in incorrect, please try again"}, 400 #error
    else:

        for i in range(len(user_data.gallery)):
            
            img_url = user_data.gallery[i]

            if img_url == photo_url:
                return {"message": "You already added this photo"}, 400
            
        else:
            user_data.gallery.append(photo_url)
            print('this is user_data: ', user_data)
            project.save()
            return {"message": "The photo was successfully saved to the account's gallery!", "data": user_data.__dict__ }  , 200
                


        # sign_In = Sign_In_Page(userdata,project.accountDict)
        # search_result = sign_In.search_photo(data["search"])
        # if search_result:
        #     userdata.gallery[data["search"]] = data["link"]
        #     project.save()
        #     return {"message": "The photo was successfully saved to the account's gallery!", "data": userdata["gallery"] }  , 200
        # else:
        #     return {"message": "Did not find the photo you were looking for"}, 400


@app.route('/update-account', methods=['POST'])
def update_account():
    data = request.get_json()
    account_existed , userdata = project.sign_in(data["username"],data["password"])
    if account_existed:
        return {"message":"The username of the password you've entered in incorrect, please try again"}, 400 #error
    else:
        sign_In = Sign_In_Page(userdata,project.accountDict)
        update_result = sign_In.update_account(data["new_username"],data["new_password"],data["new_email"])
        if update_result:
            return {"message":"The username already existis, please try another username"}, 400
        else:
            project.save()
            return {"message": "Your account was updated!" , "data": userdata.__dict__  } , 200


@app.route('/update-account', methods=['POST'])
def delete_account():
    data = request.get_json()
    account_existed , userdata = project.sign_in(data["username"],data["password"])
    if account_existed:
        return {"message":"The username of the password you've entered in incorrect, please try again"}, 400 #error
    else:
        sign_In = Sign_In_Page(userdata,project.accountDict)
        delete_result = sign_In.delete_account(data["password"])
        if delete_result:
            return {"message":"There was an error deleting your account, please try again"}, 400
        else:
            project.save()
            return {"message": "Your account has been successfully deleted!" } , 200


if __name__ == "__main__":
    project = Application()
    project.load()
    # print(project)
    app.run(debug=True)
    

# from main_menu import Main_Menu
# if __name__ == "__main__":
    # main_menu=Main_Menu()
    # main_menu.run()

