import os
from flask import Flask

app1 = Flask(__name__)

@app1.route('/')
def hello():
    return "IYOO NIAANNN APOO !!!"

if __name__ == '__main__':
    app1.run(debug = True, host = os.getenv('HOST'), port = os.getenv('PORT2'))