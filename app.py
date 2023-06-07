from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! This is online in Azure now!</p>"

@app.route("/flasktest")
def flask_test():
    return "<p>This is a test to see how to commit with continous deployment works!</p>"