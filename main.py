from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from application import Application

from flask_cors import CORS, cross_origin
cors = CORS(app)


@app.route('/sign-up', methods=['POST'])
def sign_up():
    data = request.get_json()
    print(data)
    print("YOOooooooooooooooo________________")
    print(project)
    x = project.sign_up(data["username"],data["password"],data["email"])
    return {"message":x}


@app.route('/login', methods=['GET'])
def login():

    return jsonify({"data": "this is a data from login page"}), 201


@app.route('/search-photo', methods=['GET'])
def search_photo():

    print('this is a sign-up')
    return "12"


@app.route('/save-photo', methods=['POST'])
def save_photo():

    print('this is a sign-up')
    return "12"


@app.route('/change-username', methods=['POST'])
def change_username():

    print('this is a sign-up')
    return "12"


@app.route('/change-email', methods=['POST'])
def change_email():

    pass


@app.route('/change-password', methods=['POST'])
def change_password():

    pass


@app.route('/delete-account', methods=['POST'])
def delete_account():

    pass


if __name__ == "__main__":
    project = Application()
    project.load()
    print(project)
    app.run(debug=True)
    

# from main_menu import Main_Menu
# if __name__ == "__main__":
    # main_menu=Main_Menu()
    # main_menu.run()

