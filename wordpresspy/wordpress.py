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

    def __init__(self, **kwargs):
        kwargs['url_prefix'] = '/wp-json/wp/v2'
        self.api = API(**kwargs)

    def create_post(self, **kwargs):
        return json.loads(self.api.post('/posts', json.dumps({
            'author': kwargs.get('author', 0),
            'content': kwargs.get('content', ''),
            'excerpt': kwargs.get('excerpt', ''),
            'slug': kwargs.get('slug', str_to_slug(kwargs.get('title'))),
            'status': kwargs.get('status', POST_STATUS_PUBLISH),
            'title': kwargs.get('title')
        })))

    def create_media(self, binary, filename, **kwargs):
        res = json.loads(self.api.upload('/media', binary, filename))
        self.update_media(res['id'], **kwargs)
        return res

    def delete_media(self, id):
        return json.loads(self.api.delete('/media/' + str(id), json.dumps({
            'force': True
        })))

    def get_media(self, id):
        return json.loads(self.api.get('/media/' + str(id)))

    def list_media(self):
        return json.loads(self.api.get('/media'))

    def update_media(self, id, **kwargs):
        return json.loads(self.api.post('/media/' + str(id), json.dumps({
            'alt_text': kwargs.get('alt_text', ''),
            'caption': kwargs.get('caption', ''),
            'description': kwargs.get('description', ''),
            'title': kwargs.get('title', '')
        })))
