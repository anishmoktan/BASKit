# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/home')
# def index():
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True)
from main_menu import Main_Menu
if __name__ == "__main__":
    main_menu=Main_Menu()
    main_menu.run()


