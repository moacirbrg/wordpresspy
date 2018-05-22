import json

from .api import API

class WordPressAPI:
    api = None

    def __init__(self, domain, port, username, password):
        self.api = API(domain, port, username, password, url_prefix='/wp-json/wp/v2')

    def create_post(self, **kwargs):
        return json.loads(self.api.post('/posts', json.dumps({
            'title': kwargs.get('title'),
            'content': kwargs.get('content', ''),
            'excerpt': kwargs.get('excerpt', '')
        })))
