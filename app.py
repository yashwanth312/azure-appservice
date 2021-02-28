from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello,<b>Yashwanth</b>   <img src='https://storageyashapp.blob.core.windows.net/mycontainer/1.jpg' width='200'  height='200' />"

