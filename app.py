from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome_msg():
    return 'Welcome to python flask web application'

if __name__ == '__main__':
    app.run()
