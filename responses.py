class BaseResponse:
    default_status = '200'
    default_content_type = 'text/plain;'

    def __init__(self, body=None, status=None, headers=None):
        self.body = body if body else [b'']
        self.status_code = status or self.default_status
        self.headers = [('Content-type', 'text/plain; charset=utf-8')]


class Response(BaseResponse):
    default_content_type = 'text/plain; charset=UTF-8'

    def __init__(self, body='', status=None, headers=None, charset='utf-8'):
        self.charset = charset
        self._body = body
        if isinstance(body, str):
            self._body = body.encode(self.charset)
        super().__init__([self._body], status, headers)


    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        if isinstance(value, str):
            self._body = [value.encode(self.charset)]
        if isinstance(value, bytes):
            self._body = [value]