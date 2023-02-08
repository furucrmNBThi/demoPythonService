from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os
import time

def test(environ, start_response):
    print("app is running")
    time.sleep(5)
    response_body = 'Hello World'
    status = '200 OK'

    response_headers = [('Content-Type', 'text/plain'),
                           ('Content-Length', str(len(response_body)))]

    start_response(status, response_headers)
    return [response_body]

def hello_world(request):
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "world"
    message = "Hello, " + name + "!\n"
    return Response(message)


if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, test)
    server.serve_forever()
