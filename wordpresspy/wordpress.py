import json

from .api import API
from .utils import create_json_without_nulls

POST_FORMAT_ASIDE = 'aside'
POST_FORMAT_AUDIO = 'audio'
POST_FORMAT_CHAT = 'chat'
POST_FORMAT_GALLERY = 'gallery'
POST_FORMAT_IMAGE = 'image'
POST_FORMAT_LINK = 'link'
POST_FORMAT_QUOTE = 'quote'
POST_FORMAT_STANDARD = 'standard'
POST_FORMAT_STATUS = 'status'
POST_FORMAT_VIDEO = 'video'

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

    def _create_category_entity(self, **kwargs):
        return {
            'description': kwargs.get('description', None),
            'name': kwargs.get('name', None),
            'slug': kwargs.get('slug', None),
            'parent': kwargs.get('parent', None)
        }

    def create_category(self, **kwargs):
        post = self._create_category_entity(**kwargs)
        post = create_json_without_nulls(post)
        return json.loads(self.api.post('/categories', json.dumps(post)))

    def update_category(self, id, **kwargs):
        category = self._create_category_entity(**kwargs)
        category = create_json_without_nulls(category)
        return json.loads(self.api.post('/categories/' + str(id),
                          json.dumps(category)))

    def delete_category(self, id):
        return json.loads(self.api.delete('/categories/' + str(id),
                          json.dumps({'force': True})))

    def get_category(self, id):
        return json.loads(self.api.get('/categories/' + str(id)))

    def get_categories(self):
        return json.loads(self.api.get('/categories'))

    def _create_media_entity(self, **kwargs):
        return {
            'alt_text': kwargs.get('alt_text', None),
            'author': kwargs.get('author', None),
            'caption': kwargs.get('caption', None),
            'date': kwargs.get('date', None),
            'description': kwargs.get('description', None),
            'title': kwargs.get('title', None)
        }

    def create_media(self, binary, filename, **kwargs):
        res = json.loads(self.api.upload('/media', binary, filename))
        self.update_media(res['id'], **kwargs)
        return res

    def update_media(self, id, **kwargs):
        media = self._create_media_entity(**kwargs)
        media = create_json_without_nulls(media)
        return json.loads(self.api.post('/media/' + str(id),
                          json.dumps(media)))

    def delete_media(self, id):
        return json.loads(self.api.delete('/media/' + str(id), json.dumps({
            'force': True
        })))

    def get_media(self, id):
        return json.loads(self.api.get('/media/' + str(id)))

    def get_medias(self):
        return json.loads(self.api.get('/media'))
    
    def _create_post_entity(self, **kwargs):
        return {
            'author': kwargs.get('author', None),
            'categories': kwargs.get('categories', None),
            'content': kwargs.get('content', None),
            'date': kwargs.get('date', None),
            'excerpt': kwargs.get('excerpt', None),
            'featured_media': kwargs.get('featured_media', None),
            'format': kwargs.get('format', None),
            'slug': kwargs.get('slug', None),
            'status': kwargs.get('status', None),
            'tags': kwargs.get('tags', None),
            'title': kwargs.get('title', None)
        }

    def create_post(self, **kwargs):
        post = self._create_post_entity(**kwargs)
        post = create_json_without_nulls(post)
        return json.loads(self.api.post('/posts', json.dumps(post)))

    def update_post(self, id, **kwargs):
        post = self._create_post_entity(**kwargs)
        post = create_json_without_nulls(post)
        return json.loads(self.api.post('/posts/' + str(id),
                          json.dumps(post)))

    def delete_post(self, id):
        return json.loads(self.api.delete('/posts/' + str(id)))

    def get_post(self, id):
        return json.loads(self.api.get('/posts/' + str(id)))

    def get_posts(self):
        return json.loads(self.api.get('/posts'))
