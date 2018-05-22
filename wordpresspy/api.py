import base64
import http.client
from os.path import basename

from .http_method import HTTP_DELETE, HTTP_GET, HTTP_POST, HTTP_PUT


class API:
    conn = None

    def __init__(self, domain, port, username, password, url_prefix=''):
        self.username = username
        self.password = password
        self.domain = domain
        self.port = port
        self.url_prefix = url_prefix

    def _get_access_token(self):
        userpass = bytearray('%s:%s' % (self.username, self.password), 'utf8')
        return base64.b64encode(userpass).decode('utf8')

    def _get_connection(self):
        if (self.conn is None):
            self.conn = http.client.HTTPConnection(self.domain, self.port)
        return self.conn

    def _get_headers(self):
        return {
            'Authorization': 'Basic ' + self._get_access_token()
        }

    def _get_json_headers(self):
        headers = self._get_headers()
        headers['Content-type'] = 'application/json'
        return headers

    def _get_upload_headers(self, filename):
        headers = self._get_headers()
        headers['Content-Disposition'] = 'form-data; filename="%s"' % filename
        return headers

    def _get_url(self, url):
        return self.url_prefix + url

    def _request(self, method, url, data=None):
        conn = self._get_connection()
        url = self._get_url(url)
        headers = self._get_json_headers()
        conn.request(method, url, body=data, headers=headers)
        return conn.getresponse().read()

    def upload(self, url, file_binary):
        conn = self._get_connection()
        url = self._get_url(url)
        headers = self._get_upload_headers(basename(file_binary.name))
        method = HTTP_POST
        conn.request(method, url, body=file_binary, headers=headers)
        return conn.getresponse().read()

    def delete(self, url):
        return self._request(HTTP_DELETE, url)

    def get(self, url):
        return self._request(HTTP_GET, url)

    def post(self, url, data):
        return self._request(HTTP_POST, url, data)

    def put(self, url, data):
        return self._request(HTTP_PUT, url, data)
