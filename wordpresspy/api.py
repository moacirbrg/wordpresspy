import base64
import urllib.request

from .http_method import HTTP_DELETE, HTTP_GET, HTTP_POST, HTTP_PUT


class API:
    domain = None
    port = 80
    ssl = False
    username = None
    password = None
    url_prefix = ''

    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.domain = kwargs.get('domain')
        self.port = kwargs.get('port', self.port)
        self.ssl = kwargs.get('ssl', self.ssl)
        self.url_prefix = kwargs.get('url_prefix', self.url_prefix)

    def _get_access_token(self):
        userpass = bytearray('%s:%s' % (self.username, self.password), 'utf8')
        return base64.b64encode(userpass).decode('utf8')

    def _get_url(self, url):
        full_url = 'http://' if self.ssl is False else 'https://'
        full_url += self.domain
        full_url += ":" + str(self.port)
        full_url += self.url_prefix
        full_url += url
        return full_url

    def _request(self, method, url, data=None):
        url = self._get_url(url)
        req = urllib.request.Request(url=url, data=data, method=method)
        req.add_header('Authorization', 'Basic ' + self._get_access_token())
        req.add_header('Content-type', 'application/json')
        res = urllib.request.urlopen(req)
        return res.read()

    def upload(self, url, binary, filename):
        url = self._get_url(url)
        req = urllib.request.Request(url=url, data=binary, method=HTTP_POST)
        req.add_header('Authorization', 'Basic ' + self._get_access_token())
        req.add_header('Content-Disposition',
                       'form-data; filename="%s"' % filename)
        res = urllib.request.urlopen(req)
        return res.read()

    def delete(self, url):
        return self._request(HTTP_DELETE, url)

    def get(self, url):
        return self._request(HTTP_GET, url)

    def post(self, url, data):
        return self._request(HTTP_POST, url, bytes(data, 'utf-8'))

    def put(self, url, data):
        return self._request(HTTP_PUT, url, bytes(data, 'utf-8'))
