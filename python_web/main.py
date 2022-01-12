from flask import Flask
import subprocess as sp


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8081)
