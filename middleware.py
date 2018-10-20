# from flask_restful import inputs, abort

class SimpleMiddleware(object):

    def __init__(self, app):
        self.app =app
    
    def __call__(self, environ, start_response):
        print(environ)
        
        if (environ['PATH_INFO'] == '/api/v1/komponen/readAllkomponenData'):
            return self.app(environ, start_response)
        
        if (environ['PATH_INFO'] == '/api/v1/komponen/readOneUserkomponenData'):
            return self.app(environ,start_response)

        

        if (environ['HTTP_AUTHORIZATION'] != 'qwerty'):
            return self.app(environ, start_response('400 CING balek Atuh euy', [("Content-Type", "text/html")]))
            # return abort (404, message = '404 CING balek Atuh euy')
        return self.app(environ, start_response)
        