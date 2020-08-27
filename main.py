from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/sign-up', methods=['POST'])
def sign_up():
    data = request.get_json()
    x = project.sign_up(data["username"], data["password"], data["email"])
    if x:
        return {"message":"An account with the username and/or email"{username} {"password"} {email}")
    project.save()
    return {"message": x}
@app.route('/login', methods=['GET'])
def login():
    data = request.get_json()
    x = project.sign_up(data["username"], data["password"], data["email"])
    if x:
        return
    else:
        return
    
    return

@app.route('/search-photo', methods=['GET'])
def search_photo():
    data = request.get_json()
    return


@app.route('/save-photo', methods=['POST'])
def save_photo():
    data = request.get_json()
    Be_answer , userdata = project.sign_in(data["username"], data["password"])
    if Be_answer:
        return{"message": "The username of the password you've entered, please try again"}, 400 #error
    else:
        sign_In =Sign_In




@app.route('/update-account', methods=['POST'])
def chang():
    return

@app.route('/delete-account', methods=['POST'])
def delete_account():
    data = request.get_json()

    return

if __name__ == "__main__":
    app.run(debug=True)

