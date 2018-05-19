import base64
import http.client
from enum import Enum
from os.path import basename


class API:
    conn = None

    def __init__(self, domain, port, username, password, url_prefix=''):
        self.username = username
        self.password = password
        self.domain = domain
        self.port = port
        self.url_prefix = url_prefix

    def __get_access_token(self):
        userpass = bytearray('%s:%s' % (self.username, self.password), 'utf8')
        return base64.b64encode(userpass).decode('utf8')

    def __get_connection(self):
        if (self.conn is None):
            self.conn = http.client.HTTPConnection(self.domain, self.port)
        return self.conn

    def __get_headers(self):
        return {
            'Authorization': 'Basic ' + self.__get_access_token()
        }

    def __get_json_headers(self):
        headers = self.__get_headers()
        headers['Content-type'] = 'application/json'
        return headers

    def __get_upload_headers(self, filename):
        headers = self.__get_headers()
        headers['Content-Disposition'] = 'form-data; filename="%s"' % filename
        return headers

    def __get_url(self, url):
        return self.url_prefix + url

    def __request(self, method, url, data=None):
        conn = self.__get_connection()
        url = self.__get_url(url)
        headers = self.__get_json_headers()
        conn.request(method, url, body=data, headers=headers)
        return conn.getresponse().read()

    def upload(self, url, file_binary):
        conn = self.__get_connection()
        url = self.__get_url(url)
        headers = self.__get_upload_headers(basename(file_binary.name))
        method = HTTP_Method.POST.value
        conn.request(method, url, body=file_binary, headers=headers)
        return conn.getresponse().read()

    def delete(self, url):
        return self.__request(HTTP_Method.DELETE.value, url)

    def get(self, url):
        return self.__request(HTTP_Method.GET.value, url)

    def post(self, url, data):
        return self.__request(HTTP_Method.POST.value, url, data)

    def put(self, url, data):
        return self.__request(HTTP_Method.PUT.value, url, data)


class HTTP_Method(Enum):
    DELETE = 'DELETE'
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
