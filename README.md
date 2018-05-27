# WordPressPy
WordPressPy is a Python library for automate management in WordPress installations including its plugins as WooCommerce.

* [Installation](#installation)
* [WordPress](#wordpress)
  * [WordPress connnection](#wordpress-connnection)
  * [Post](#post)
    * [Create post](#create-post)
    * [Update post](#update-post)
    * [Delete post](#delete-post)
    * [Get post](#get-post)
    * [List post](#list-post)
  * [Media](#media)
    * [Create media](#create-media)
    * [Update media](#update-media)
    * [Delete media](#update-media)
    * [Get media](#get-media)
    * [List media](#list-media)
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
```

Returns one [Post Schema](#post).

#### List post
```python3
posts = wpapi.list_post()
```

Returns a list of [Post Schema](#post).

### Media
The following methods helps you to manage medias.<br/>
You can find details about fields of Media Schema on https://developer.wordpress.org/rest-api/reference/posts/#schema

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
```

Returns one [Media Schema](#media).

#### List media
```python3
medias = wpapi.list_media()
```

Returns a list of [Media Schema](#media).

## Errors
WordPressPy can raise the following errors:

### WordPressError
Error properties:
* **reason**: Error message (string)
* **http_status**: HTTP Status Code (int)
```python3
from wordpresspy.errors import WordPressError
```