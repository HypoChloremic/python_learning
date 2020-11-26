# Remember to read the main learning markdown file
# To run the app in Windows, from command line, CMD:
# >>> set FLASK_APP=helloworld_app.py
# in PowerShell
# >>> $env:FLASK_APP=helloworld_app.py
# Subsequently:
# >>> python -m flask run 

from flask import Flask
from markupsafe import escape

app = Flask(__name__)
@app.route('/') # This tells Flask what url triggers the function
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

################################
##### PLAYING WITH THE URL #####
##### API STYLE            #####
################################
# the '<username>' makes username a variable symbol
# accessible inside the function. 
# Noting however, that the variable symbol is the same
# as the arg being passed to the function. 
# 
# Available converter types:
# string: (default) accepts any text without a slash
# int: accepts positive integers
# float: accepts positive floating point values
# path: like string but also accepts slashes
# uuid: accepts UUID strings

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'