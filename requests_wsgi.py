class Request:
    """wrapper for WSGI environ dictionary"""

    def __init__(self, environ=None):
        self.environ = {} if environ is None else environ
        self.content = self.get_content()

    def get(self, value, default=None):
        return self.environ.get(value, default)

    @property
    def path(self):
        return self.environ.get('PATH_INFO', '')

    @property
    def method(self):
        return self.environ.get('REQUEST_METHOD', 'GET').upper()

    def get_content(self):
        if 'wsgi.input' in self.environ:
            content = self.environ['wsgi.input'].read().decode()
        else:
            content = None
        return content