import re
import unicodedata
from six import string_types


def remove_special_chars(s):
    if not isinstance(s, string_types):
        return s
    else:
        return re.sub('[^a-zA-Z0-9 \n\.]', '', s)


def str_to_ascii(s):
    if not isinstance(s, string_types):
        return s
    else:
        return unicodedata \
            .normalize('NFKD', s) \
            .encode('ascii', 'ignore') \
            .decode('utf8')


def str_to_slug(s):
    if not isinstance(s, string_types):
        return s
    else:
        slug = s.lower()
        slug = str_to_ascii(slug)
        slug = remove_special_chars(slug)
        slug = slug.replace(' ', '-')
        return slug
