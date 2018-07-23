import json

from .api import API
from .utils import create_json_without_nulls, get_property

CATALOG_VISIBILITY_VISIBLE = 'visible'
CATALOG_VISIBILITY_CATALOG = 'catalog'
CATALOG_VISIBILITY_SEARCH = 'search'
CATALOG_VISIBILITY_HIDDEN = 'hidden'

PRODUCT_STATUS_DRAFT = 'draft'
PRODUCT_STATUS_PENDING = 'pending'
PRODUCT_STATUS_PRIVATE = 'private'
PRODUCT_STATUS_PUBLISH = 'publish'

PRODUCT_TYPE_SIMPLE = 'simple'
PRODUCT_TYPE_GROUPED = 'grouped'
PRODUCT_TYPE_external = 'external'
PRODUCT_TYPE_variable = 'variable'

TAX_STATUS_TAXABLE = 'taxable'
TAX_STATUS_SHIPPING = 'shipping'
TAX_STATUS_NONE = 'none'


class WooCommerceAPI:
    api = None

    def __init__(self, **kwargs):
        kwargs['url_prefix'] = '/wp-json/wc/v2'
        self.api = API(**kwargs)

    def _create_product_attributes(self, items):
        if not isinstance(items, list):
            return items

        properties = []
        for item in items:
            if isinstance(item, dict):
                fullprops = {
                    'id': get_property(item, 'id', None),
                    'name': get_property(item, 'name', None),
                    'position': get_property(item, 'position', None),
                    'visible': get_property(item, 'visible', None),
                    'variation': get_property(item, 'variation', None),
                    'options': get_property(item, 'options', None)
                }
                properties.append(create_json_without_nulls(fullprops))
        return properties

    def _create_product_categories(self, items):
        if not isinstance(items, list):
            return items

        properties = []
        for item in items:
            if isinstance(item, dict):
                properties.append({
                    'id': get_property(item, 'id', None)
                })
        return properties

    def _create_product_default_attributes(self, items):
        if not isinstance(items, list):
            return items

        properties = []
        for item in items:
            if isinstance(item, dict):
                properties.append({
                    'id': get_property(item, 'id', None),
                    'name': get_property(item, 'name', None),
                    'option': get_property(item, 'option', None)
                })
        return properties

    def _create_product_dimensions(self, items):
        if not isinstance(items, list):
            return items

        properties = []
        for item in items:
            if isinstance(item, dict):
                properties.append({
                    'length': get_property(item, 'length', None),
                    'width': get_property(item, 'width', None),
                    'height': get_property(item, 'height', None)
                })
        return properties

    def _create_product_downloads(self, items):
        if not isinstance(items, list):
            return items

        properties = []
        for item in items:
            if isinstance(item, dict):
                properties.append({
                    'name': get_property(item, 'name', None),
                    'file': get_property(item, 'file', None)
                })
        return properties

    def _create_product_images(self, items):
        if not isinstance(items, list):
            return items

        properties = []
        for item in items:
            if isinstance(item, dict):
                fullprops = {
                    'id': get_property(item, 'id', None),
                    'src': get_property(item, 'src', None),
                    'name': get_property(item, 'name', None),
                    'alt': get_property(item, 'alt', None),
                    'position': get_property(item, 'position', None)
                }
                properties.append(create_json_without_nulls(fullprops))
        return properties

    def _create_product_meta_data(self, items):
        if not isinstance(items, list):
            return items

        properties = []
        for item in items:
            if isinstance(item, dict):
                properties.append({
                    'key': get_property(item, 'key', None),
                    'value': get_property(item, 'value', None)
                })
        return properties

    def _create_product_entity(self, **kwargs):
        return {
            'name': kwargs.get('name', None),
            'slug': kwargs.get('slug', None),
            'type': kwargs.get('type', None),
            'status': kwargs.get('status', None),
            'featured': kwargs.get('featured', None),
            'catalog_visibility': kwargs.get('catalog_visibility', None),
            'description': kwargs.get('description', None),
            'short_description': kwargs.get('short_description', None),
            'sku': kwargs.get('sku', None),
            'regular_price': kwargs.get('regular_price', None),
            'sale_price': kwargs.get('sale_price', None),
            'date_on_sale_from': kwargs.get('date_on_sale_from', None),
            'date_on_sale_from_gmt': kwargs.get('date_on_sale_from_gmt', None),
            'date_on_sale_to': kwargs.get('date_on_sale_to', None),
            'date_on_sale_to_gmt': kwargs.get('date_on_sale_to_gmt', None),
            'virtual': kwargs.get('virtual', None),
            'downloadable': kwargs.get('downloadable', None),
            'downloads': self._create_product_downloads(
                kwargs.get('downloads', None)),
            'download_limit': kwargs.get('download_limit', None),
            'download_expiry': kwargs.get('download_expiry', None),
            'external_url': kwargs.get('external_url', None),
            'button_text': kwargs.get('button_text', None),
            'tax_status': kwargs.get('tax_status', None),
            'tax_class': kwargs.get('tax_class', None),
            'manage_stock': kwargs.get('manage_stock', None),
            'stock_quantity': kwargs.get('stock_quantity', None),
            'in_stock': kwargs.get('in_stock', None),
            'backorders': kwargs.get('backorders', None),
            'sold_individually': kwargs.get('sold_individually', None),
            'weight': kwargs.get('weight', None),
            'dimensions': self._create_product_dimensions(
                kwargs.get('dimensions', None)),
            'shipping_class': kwargs.get('shipping_class', None),
            'reviews_allowed': kwargs.get('reviews_allowed', None),
            'upsell_ids': kwargs.get('upsell_ids', None),
            'cross_sell_ids': kwargs.get('cross_sell_ids', None),
            'parent_id': kwargs.get('parent_id', None),
            'purchase_note': kwargs.get('purchase_note', None),
            'categories': self._create_product_categories(
                kwargs.get('categories', None)),
            'attributes': self._create_product_attributes(
                kwargs.get('attributes', None)),
            'default_attributes': self._create_product_default_attributes(
                kwargs.get('default_attributes', None)),
            'grouped_products': kwargs.get('grouped_products', None),
            'menu_order': kwargs.get('menu_order', None),
            'meta_data': self._create_product_meta_data(
                kwargs.get('meta_data', None)),
            'images': self._create_product_images(
                kwargs.get('images', None))
        }

    def _create_products_query_params(self, **kwargs):
        return {
            'context': kwargs.get('context', None),
            'page': kwargs.get('page', None),
            'per_page': kwargs.get('per_page', None),
            'search': kwargs.get('search', None),
            'after': kwargs.get('after', None),
            'before': kwargs.get('before', None),
            'exclude': kwargs.get('exclude', None),
            'include': kwargs.get('include', None),
            'offset': kwargs.get('offset', None),
            'order': kwargs.get('order', None),
            'orderby': kwargs.get('orderby', None),
            'parent_exclude': kwargs.get('parent_exclude', None),
            'slug': kwargs.get('slug', None),
            'type': kwargs.get('type', None),
            'sku': kwargs.get('sku', None),
            'featured': kwargs.get('featured', None),
            'category': kwargs.get('category', None),
            'tag': kwargs.get('tag', None),
            'attribute': kwargs.get('attribute', None),
            'shipping_class': kwargs.get('shipping_class', None),
            'attribute_term': kwargs.get('attribute_term', None),
            'tax_class': kwargs.get('tax_class', None),
            'in_stock': kwargs.get('in_stock', None),
            'on_sale': kwargs.get('on_sale', None),
            'min_price': kwargs.get('min_price', None),
            'max_price': kwargs.get('max_price', None)
        }

    def _create_entity(self, url, entity):
        entity = create_json_without_nulls(entity)
        return json.loads(self.api.post(url, json.dumps(entity)))

    def _update_entity(self, url, entity):
        entity = create_json_without_nulls(entity)
        return json.loads(self.api.put(url, json.dumps(entity)))

    def _get_entities(self, url, **kwargs):
        query_params = self._create_products_query_params(**kwargs)
        query_params_without_nulls = create_json_without_nulls(query_params)
        return json.loads(self.api.get(url, query_params_without_nulls))

    def create_product(self, **kwargs):
        entity = self._create_product_entity(**kwargs)
        return self._create_entity('/products', entity)

    def update_product(self, id, **kwargs):
        entity = self._create_product_entity(**kwargs)
        return self._update_entity('/products/' + str(id), entity)

    def get_product(self, id):
        return self._get_entities('/products/' + str(id))

    def get_products(self, **kwargs):
        return self._get_entities('/products', **kwargs)
