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
        if isinstance(body, str):
            body = body.encode(charset)
        iterable_body = [body]
        super().__init__(iterable_body, status, headers)
        self.charset = charset
