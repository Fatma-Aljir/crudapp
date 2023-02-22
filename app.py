# render_template allows us to return a html output with desired data
import sqlite3

from flask import Flask, render_template

# app references the object from the flask package
# creating a flask application instance
app = Flask(__name__)
# by creation of the instance above . we can use it to handle incoming web requests and send responses to users

# app.route this is called a decorator , turns a regular python functon into a flask view(user can see elements) functions
# The flask view function : converts the function retuen value into a HTTP response to be displayed by aHTTP client
# such as a web browser
# decoratoe markup : @app.route('/')
#@app.route('/')
#def hello_world():  # put application's code here
   # return 'Hello World!'






# create a cnnection to our sqlite.db
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# DEFINING THE ROUTE FOR DISPLAYING THE POSTS
@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run()
