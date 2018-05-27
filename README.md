# WordPressPy
WordPressPy is a Python library for automate management in WordPress installations including its plugins as WooCommerce.

* [Installation](#installation)
* [WordPress](#wordpress)
  * [WordPress connnection](#wordpress-connnection)
  * [Posts](#posts)
    * [Create post](#create-post)
  * [Medias](#medias)
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
|POST_STATUS_PUBLISH    | 'publish'     |
|POST_STATUS_FUTURE     | 'future'      |
|POST_STATUS_DRAFT      | 'draft'       |
|POST_STATUS_PENDING    | 'pending'     |
|POST_STATUS_PRIVATE    | 'private'     |


### Posts
The following methods helps you to manage posts.

#### Create post
```python3
wpapi.create_post(
  author=0,
  content='My post full content',
  excerpt='My post description',
  slug='my-post-url',
  status=POST_STATUS_PUBLISH,
  title='My post Title'
)
```

|Field      | Note                                                                |
|:----------|:--------------------------------------------------------------------|
|author     | Author ID                                                           |
|slug       | Default value is title to lower case, replace non-ascii chars to ascii candidate, non-repleceable special chars removed and replace white space to slash.                                         |
|title     | Title is mandatory                                                   |

### Medias
The following methods helps you to manage medias.

#### Create media
For create a media you need to pass the image binary, however there are many ways to load images. Follows some examples:
```python3
# Upload from your disk
from os.path import basename

path = 'path-of-images-folder/image-name.extension'
binary = open(path, 'rb')

...

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
wpapi.get_media(media_id)
```

Returns a parsed JSON from WordPress REST API.

#### List media
```python3
wpapi.list_media()
```

Returns a list of *Get media* result.

## Errors
WordPressPy can raise the following errors:

### WordPressPyError
Error properties:
* **reason**: Error message (string)
* **http_status**: HTTP Status Code (int)
```python3
from wordpresspy.errors import WordPressPyError
```