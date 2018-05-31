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

STATUS_PUBLISH = 'publish'
STATUS_FUTURE = 'future'
STATUS_DRAFT = 'draft'
STATUS_PENDING = 'pending'
STATUS_PRIVATE = 'private'


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

    def _create_media_entity(self, **kwargs):
        return {
            'alt_text': kwargs.get('alt_text', None),
            'author': kwargs.get('author', None),
            'caption': kwargs.get('caption', None),
            'date': kwargs.get('date', None),
            'description': kwargs.get('description', None),
            'title': kwargs.get('title', None)
        }

    def _create_page_entity(self, **kwargs):
        return {
            'author': kwargs.get('author', None),
            'content': kwargs.get('content', None),
            'date': kwargs.get('date', None),
            'date_gmt': kwargs.get('date_gmt', None),
            'featured_media': kwargs.get('featured_media', None),
            'menu_order': kwargs.get('menu_order', None),
            'meta': kwargs.get('meta', None),
            'parent': kwargs.get('parent', None),
            'password': kwargs.get('password', None),
            'slug': kwargs.get('slug', None),
            'status': kwargs.get('status', None),
            'template': kwargs.get('template', None),
            'title': kwargs.get('title', None)
        }

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

    def _create_tag_entity(self, **kwargs):
        return {
            'description': kwargs.get('description', None),
            'name': kwargs.get('name', None),
            'slug': kwargs.get('slug', None)
        }

    def _save_entity(self, url, entity):
        entity = create_json_without_nulls(entity)
        return json.loads(self.api.post(url, json.dumps(entity)))

    def _delete_entity(self, url, force=False):
        force_param = None if force is False else json.dumps({'force': True})
        return json.loads(self.api.delete(url, force_param))

    def _get_entity(self, url):
        return json.loads(self.api.get(url))

    def _get_entities(self, url):
        return json.loads(self.api.get(url))

    def create_category(self, **kwargs):
        entity = self._create_category_entity(**kwargs)
        return self._save_entity('/categories', entity)

    def update_category(self, id, **kwargs):
        entity = self._create_category_entity(**kwargs)
        return self._save_entity('/categories/' + str(id), entity)

    def delete_category(self, id):
        return self._delete_entity('/categories/' + str(id), True)

    def get_category(self, id):
        return self._get_entity('/categories/' + str(id))

    def get_categories(self):
        return self._get_entities('/categories')

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
        return self._delete_entity('/media/' + str(id), True)

    def get_media(self, id):
        return self._get_entity('/media/' + str(id))

    def get_medias(self):
        return self._get_entities('/media')

    def create_page(self, **kwargs):
        entity = self._create_page_entity(**kwargs)
        return self._save_entity('/pages', entity)

    def update_page(self, id, **kwargs):
        entity = self._create_page_entity(**kwargs)
        return self._save_entity('/pages/' + str(id), entity)

    def delete_page(self, id):
        return self._delete_entity('/pages/' + str(id))

    def get_page(self, id):
        return self._get_entity('/pages/' + str(id))

    def get_pages(self):
        return self._get_entities('/pages')

    def create_post(self, **kwargs):
        entity = self._create_post_entity(**kwargs)
        return self._save_entity('/posts', entity)

    def update_post(self, id, **kwargs):
        entity = self._create_post_entity(**kwargs)
        return self._save_entity('/posts/' + str(id), entity)

    def delete_post(self, id):
        return self._delete_entity('/posts/' + str(id))

    def get_post(self, id):
        return self._get_entity('/posts/' + str(id))

    def get_posts(self):
        return self._get_entities('/posts')

    def get_post_revisions(self, id):
        return self._get_entities('/posts/' + str(id) + '/revisions')

    def delete_post_revision(self, post_id, revision_id):
        url = '/posts/' + str(post_id) + '/revisions/' + str(revision_id)
        return self._delete_entity(url, True)

    def create_tag(self, **kwargs):
        entity = self._create_tag_entity(**kwargs)
        return self._save_entity('/tags', entity)

    def update_tag(self, id, **kwargs):
        entity = self._create_tag_entity(**kwargs)
        return self._save_entity('/tags/' + str(id), entity)

    def delete_tag(self, id):
        return self._delete_entity('/tags/' + str(id), True)

    def get_tag(self, id):
        return self._get_entity('/tags/' + str(id))

    def get_tags(self):
        return self._get_entities('/tags')
