from flask import Flask
from flask_cors import CORS
import yt_dlp
import os

app = Flask(__name__)
CORS(app)


@app.route("/")
def Hello_world():
    return "<h1>Hello</h1>"



if __name__ == '__main__':
    app.run(debug=True)