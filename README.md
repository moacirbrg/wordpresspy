# WordPressPy
WordPressPy is a Python library for automate management in WordPress installations including its plugins as WooCommerce.

* [Installation](#installation)
* [WordPress](#wordpress)
  * [WordPress connnection](#wordpress-connnection)
  * [Category](#post)
    * [Create category](#create-category)
    * [Update category](#update-category)
    * [Delete category](#delete-category)
    * [Get category](#get-category)
    * [Get categories](#get-categories)
  * [Media](#media)
    * [Create media](#create-media)
    * [Update media](#update-media)
    * [Delete media](#update-media)
    * [Get media](#get-media)
    * [Get medias](#get-medias)
  * [Post](#post)
    * [Create post](#create-post)
    * [Update post](#update-post)
    * [Delete post](#delete-post)
    * [Get post](#get-post)
    * [Get posts](#get-posts)
* [Errors](#errors)
  * [WordPressPyError](#wordpresspyerror)
    

## Configuring WordPress
For use WordPressPy you need install [Application Password](https://wordpress.org/plugins/application-passwords/), a plugin for WordPress Authentication, and configure it following their documentation page linked before.

## Installation
```bash
pip install wordpresspy
```

## WordPress
The following steps will guide you how to manage WordPress core features.

### WordPress connnection
To manage a WordPress installation you need firstly configure a connection to your WordPress.

```python3
from wordpresspy.wordpress import WordPressAPI

USERNAME = 'my-wordpress-username'
PASSWORD = 'my-user-application-password'
DOMAIN = 'my.domain.com'

wpapi = WordPressAPI(
    domain=DOMAIN,
    port=80,
    username=USERNAME,
    password=PASSWORD)
```

**NOTE**: All methods returns a parsed json from WordPress REST API.

You can also include some constants for help you to use WordPressPy.
```python3
from wordpresspy.wordpress import CONSTANT_NAME1, CONSTANT_NAME2
```
|Constant               | Value         |
|:----------------------|:--------------|
|POST_FORMAT_ASIDE      | 'aside'       |
|POST_FORMAT_AUDIO      | 'audio'       |
|POST_FORMAT_CHAT       | 'chat'        |
|POST_FORMAT_GALLERY    | 'gallery'     |
|POST_FORMAT_IMAGE      | 'image'       |
|POST_FORMAT_LINK       | 'link'        |
|POST_FORMAT_QUOTE      | 'quote'       |
|POST_FORMAT_STANDARD   | 'standard'    |
|POST_FORMAT_STATUS     | 'status'      |
|POST_FORMAT_VIDEO      | 'video'       |
|POST_STATUS_PUBLISH    | 'publish'     |
|POST_STATUS_FUTURE     | 'future'      |
|POST_STATUS_DRAFT      | 'draft'       |
|POST_STATUS_PENDING    | 'pending'     |
|POST_STATUS_PRIVATE    | 'private'     |

Besides the constants you can also include some functions to help you.
```python3
from wordpresspy.utils import str_to_slug
```

### Category
The following methods helps you to manage categories.<br/>
You can find details about fields of Category Schema on https://developer.wordpress.org/rest-api/reference/categories/#schema

#### Create category
```python3
from wordpresspy.utils import str_to_slug

...

wpapi.create_category(
  description='HTML description of the term',
  name='HTML title for the term',
  slug=str_to_slug('An unique alphanumeric identifier for the term'),
  parent=0
)
```

#### Update category
```python3
category_id = 1
wpapi.update_category(
  category_id,
  parent=16
)
```

#### Delete category
```python3
category_id = 18
wpapi.delete_category(category_id)
```

#### Get category
```python3
category_id = 18
category = wpapi.get_category(category_id)
print(category)
```

#### Get categories
```python3
categories = wpapi.get_categories()
print(categories)
```

### Media
The following methods helps you to manage medias.<br/>
You can find details about fields of Media Schema on https://developer.wordpress.org/rest-api/reference/media/#schema

#### Create media
For create a media you need to pass the image binary, however there are many ways to load images. Follows some examples:
```python3
# Upload from your disk
from os.path import basename

...

path = 'path-of-images-folder/image-name.extension'
binary = open(path, 'rb')

wpapi.create_media(
  binary,
  basename(path),
  title='Media title',
  caption='Media caption',
  description='Media description',
  alt_text='Media alternative text'
)
```

```python3
# Upload from web
import urllib.request

...

res = urllib.request.urlopen('https://some-domain.com/some-url-to-image.extension')
wpapi.create_media(
  res.read(),
  'a-name-for-image.extension',
  title='Media title',
  caption='Media caption',
  ...
  )
```

#### Update media
```python3
media_id = 1
wpapi.update_media(
  media_id,
  title='Media title',
  caption='Media caption',
  ...
)
```

#### Delete media
```python3
media_id = 1
wpapi.delete_media(media_id)
```

#### Get media
```python3
media_id = 1
media = wpapi.get_media(media_id)
print(media)
```

Returns one [Media Schema](#media).

#### Get medias
```python3
medias = wpapi.get_medias()
print(medias)
```

Returns a list of [Media Schema](#media).

### Post
The following methods helps you to manage posts.<br/>
You can find details about fields of Post Schema on https://developer.wordpress.org/rest-api/reference/posts/#schema

#### Create post
```python3
from wordpresspy.utils import str_to_slug

...

wpapi.create_post(
  author=0,
  content='My post full content',
  excerpt='My post description',
  slug=str_to_slug('My post Title'),
  status=POST_STATUS_PUBLISH,
  title='My post Title'
)
```

|Field      | Note                                                                |
|:----------|:--------------------------------------------------------------------|
|categories | Array of IDs (int). |
|date       | String with the following format: YYYY-MM-DD HH:MM:SS |
|tags       | Array of IDs (int). |

#### Update post
```python3
post_id = 1
wpapi.update_post(
  post_id,
  content='My post full content',
  title='My post Title',
  ...
)
```

#### Delete post
```python3
post_id = 1
wpapi.delete_post(post_id)
```

#### Get post
```python3
post_id = 1
post = wpapi.get_post(post_id)
print(post)
```

Returns one [Post Schema](#post).

#### Get posts
```python3
posts = wpapi.gete_posts()
print(posts)
```

Returns a list of [Post Schema](#post).

### Category
The following methods helps you to manage tags.<br/>
You can find details about fields of Tag Schema on https://developer.wordpress.org/rest-api/reference/tags/#schema

#### Create tag
```python3
from wordpresspy.utils import str_to_slug

...

wpapi.create_tag(
  description='Tag description',
  name='Tag title',
  slug=str_to_slug('Tag title'),
)
```

#### Update tag
```python3
tag_id = 22
wpapi.update_tag(
  tag_id,
  name='New name'
)
```

#### Delete tag
```python3
tag_id = 23
wpapi.delete_tag(tag_id)
```

#### Get tag
```python3
tag_id = 24
tag_id = wpapi.get_tag(tag_id)
print(tag_id)
```

#### Get tags
```python3
tags = wpapi.get_tags()
print(tags)
```

## Errors
WordPressPy can raise the following errors:

### WordPressError
Error properties:
* **reason**: Error message (string)
* **http_status**: HTTP Status Code (int)
```python3
from wordpresspy.errors import WordPressError
```
