from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os
import time
import threading

def test():
    print("app is running")
    time.sleep(5)
    return test()

def hello_world(request):
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "world"
    message = "Call outbound " + "!\n"
    return Response(message)

def start_server(app):
    server = make_server('0.0.0.0', 8080, app)
    thread = threading.Thread(target=server.serve_forever)
    thread.start()

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    start_server(app)
    test()
    
