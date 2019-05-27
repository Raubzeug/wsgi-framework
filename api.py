from requests_wsgi import Request
from responses import Response


class RoutingError(Exception):
    def __init__(self, txt):
        self.txt = txt


class API:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def wrapper(handler):
            if path in self.routes:
                raise RoutingError('{0} is already created'.format(path))
            self.routes[path] = handler
            return handler
        return wrapper

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        start_response(response.status_code, response.headers)
        return iter(response.body)

    def handle_request(self, request):
        response = Response()
        handler = self.routes.get(request.path)
        if handler is not None:
            handler(request, response)
        else:
            self.default_response(response)
        return response

    def default_response(self, response):
        response.status = '404'
        response.body = 'Not found'
