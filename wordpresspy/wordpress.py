import json

from .api import API
from .utils import str_to_slug

POST_STATUS_PUBLISH = 'publish'
POST_STATUS_FUTURE = 'future'
POST_STATUS_DRAFT = 'draft'
POST_STATUS_PENDING = 'pending'
POST_STATUS_PRIVATE = 'private'


class WordPressAPI:
    api = None

    def __init__(self, domain, port, username, password):
        url = '/wp-json/wp/v2'
        self.api = API(domain, port, username, password, url_prefix=url)

    def create_post(self, **kwargs):
        return json.loads(self.api.post('/posts', json.dumps({
            'title': kwargs.get('title'),
            'content': kwargs.get('content', ''),
            'excerpt': kwargs.get('excerpt', ''),
            'slug': kwargs.get('slug', str_to_slug(kwargs.get('title'))),
            'author': kwargs.get('author', 0),
            'status': kwargs.get('status', POST_STATUS_PUBLISH)
        })))

    def create_media(self, filepath):
        fileobj = open(filepath, 'rb')
        return json.loads(self.api.upload('/media', fileobj))
