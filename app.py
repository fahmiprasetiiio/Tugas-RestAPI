# import env
import os # memanggil env 
from flask import Flask, blueprints, request, abort
from resources.komponenData import komponenData_api
import middleware


app = Flask(__name__)
app.register_blueprint(komponenData_api, url_prefix = "/api/v1/komponen/")
app.wsgi_app = middleware.SimpleMiddleware(app.wsgi_app)

# @app.before_request
# def before_request():
#     if request.headers['Authorization'] != 'qwertyu':
#         print("LALALA")
#         return 'aaaaaaa'
#         # abort(400, message ="lololo") 

@app.route('/')
def hello():
    return "Welcome To The Most Complete Microelektra Component Center Store !"
        
if __name__ == '__main__':
    # app.run(debug = env.DEBUG, host = env.HOST, port = env.PORT)
    app.run(debug = True, host = os.getenv('HOST'), port = os.getenv('PORT1'))