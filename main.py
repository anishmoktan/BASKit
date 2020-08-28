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
    # request is the data from the frontend
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
    account_not_found , user_data = project.sign_in(username, password) 

    if account_not_found:
        return {"message":"The username of the password you've entered in incorrect, please try again"}, 400 #error
    else:
        return {"message":"You've successfully signed in to your account", "data": user_data.__dict__ } , 200


@app.route('/search-photo', methods=['POST'])
@ cross_origin()
def search_photo():
    data = request.get_json()
    username, password, search_term = data["username"], data["password"], data["searchTerm"]
    account_not_found, user_data = project.sign_in(username, password)
    
    if account_not_found:
        return {"message":"The username of the password you've entered in incorrect, please try again"}, 400 #error
    else:
        sign_in = Sign_In_Page(user_data,project.accountDict)
        search_result = sign_in.search_photo(search_term)

        if len(search_result) > 0:
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
    acount_not_found, user_data = project.sign_in(username, password)
    
    if acount_not_found:
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

@app.route('/delete-photo', methods=["POST"])
@cross_origin()
def delete_photo():
    data = request.get_json()

    username, password, photo_url = data["username"], data["password"], data["photoUrl"]
    account_not_found, user_data = project.sign_in(username, password)
    
    if account_not_found:
        return {"message":"The username of the password you've entered in incorrect, please try again"}, 400 #error
  
    else:
        user_gallery = user_data.gallery

        for i in range(len(user_gallery)):
            image_url = user_gallery[i]

            if photo_url == image_url:
                user_gallery.pop(i)
                return {"message":"Successfully delete the photo", "gallery": user_gallery}, 200 #success
                
        else:
            print("cannot find the image")
            return {"message":"Cannot find the photo"}, 400 #success



@app.route('/update-account', methods=['POST'])
@ cross_origin()
def update_account():
    data = request.get_json()
    print('this is data in update: ', data)
    old_username, old_password, old_email, new_username, new_password, new_email = data["oldUsername"], data["oldPassword"], data["oldEmail"], data["newUsername"], data["newPassword"], data["newEmail"]
    account_not_found, user_data = project.sign_in(old_username, old_password)
    
    if account_not_found:
        print('not found account')
        return {"message":"The username of the password you've entered in incorrect, please try again"}, 400 #error
    else:
        
        sign_in = Sign_In_Page(user_data, project.accountDict)
        new_user_info_found, account_info = sign_in.update_account(new_username, new_password, new_email)
        if new_user_info_found:
            print()
            return {"message":"The username already existed, please try another username"}, 400
        else:
            project.save()
            return {"message": "Your account was updated!" , "updatedAccount": account_info.__dict__  } , 200


@app.route('/delete-account', methods=['POST'])
@ cross_origin()
def delete_account():
    data = request.get_json()
    username, password = data["username"], data["password"]
    account_not_found , user_data = project.sign_in(username, password)
    if account_not_found:
        return {"message":"The username of the password you've entered in incorrect, please try again"}, 400 #error
    else:
        sign_In = Sign_In_Page(user_data,project.accountDict)
        delete_succeed = sign_In.delete_account()
        if delete_succeed:
            project.save()
            return {"message": "Your account has been successfully deleted!" } , 200
        else:
            return {"message":"There was an error deleting your account, please try again"}, 400


if __name__ == "__main__":
    project = Application()
    project.load()
    # print(project)
    app.run(debug=True)
    

# from main_menu import Main_Menu
# if __name__ == "__main__":
    # main_menu=Main_Menu()
    # main_menu.run()

