#!flask/bin/python
from flask import Flask
from flask import abort

app = Flask(__name__)
##########################################
from error import *
from router import *

# app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)