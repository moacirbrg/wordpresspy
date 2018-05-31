# WordPressPy
WordPressPy is a Python library for automate management in WordPress installations including its plugins as WooCommerce.

* [Installation](#installation)
* [WordPress](#wordpress)
  * [WordPress connnection](#wordpress-connnection)
  * [Category](#category)
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
  * [Page](#page)
    * [Create page](#create-page)
    * [Update page](#update-page)
    * [Delete page](#delete-page)
    * [Get page](#get-page)
    * [Get pages](#get-pages)
  * [Post](#post)
    * [Create post](#create-post)
    * [Update post](#update-post)
    * [Delete post](#delete-post)
    * [Get post](#get-post)
    * [Get posts](#get-posts)
  * [Post revisions](#post-revisions)
    * [Delete post revision](#delete-post-revision)
    * [Get post revisions](#get-post-revisions)
  * [Tag](#tag)
    * [Create tag](#create-tag)
    * [Update tag](#update-tag)
    * [Delete tag](#delete-tag)
    * [Get tag](#get-tag)
    * [Get tags](#get-tags)
* [Errors](#errors)
  * [WordPressError](#wordpresserror)
    

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
|STATUS_PUBLISH         | 'publish'     |
|STATUS_FUTURE          | 'future'      |
|STATUS_DRAFT           | 'draft'       |
|STATUS_PENDING         | 'pending'     |
|STATUS_PRIVATE         | 'private'     |

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

result = wpapi.create_category(
  description='HTML description of the term',
  name='HTML title for the term',
  parent=0,
  slug=str_to_slug('An unique alphanumeric identifier for the term')
)
print(result)
```

#### Update category
```python3
category_id = 28
result = wpapi.update_category(
  category_id,
  parent=1
)
print(result)
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

result = wpapi.create_media(
  binary,
  basename(path),
  title='Media title',
  caption='Media caption',
  description='Media description',
  alt_text='Media alternative text'
)
print(result)
```

```python3
# Upload from web
import urllib.request

...

res = urllib.request.urlopen('https://some-domain.com/some-url-to-image.extension')
result = wpapi.create_media(
  res.read(),
  'a-name-for-image.extension',
  title='Media title',
  caption='Media caption'
  )
print(result)
```

#### Update media
```python3
media_id = 107
result = wpapi.update_media(
  media_id,
  title='New media title',
  caption='New media caption'
)
print(result)
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

### Page
The following methods helps you to manage pages.<br/>
You can find details about fields of Page Schema on https://developer.wordpress.org/rest-api/reference/pages/#schema

#### Create page
```python3
from wordpresspy.utils import str_to_slug
from wordpresspy.wordpress import STATUS_PUBLISH

...

result = wpapi.create_page(
  author=0,
  content='Page full content',
  date='2018-01-10 00:30:00',
  featured_media=71,
  menu_order=1,
  parent=6,
  password='123456',
  slug=str_to_slug('An amazing slug of page title'),
  status=STATUS_PUBLISH,
  template='template-homepage.php',
  title='An amazing page title'
)
print(result)
```

#### Update page
```python3
page_id = 105
result = wpapi.update_page(
  page_id,
  content='New full content'
)
print(result)
```

#### Delete page
```python3
page_id = 105
wpapi.delete_page(page_id)
```

#### Get page
```python3
page_id = 7
page = wpapi.get_page(page_id)
print(page)
```

Returns one [Page Schema](#page).

#### Get pages
```python3
pages = wpapi.get_pages()
print(pages)
```

Returns a list of [Page Schema](#page).

### Post
The following methods helps you to manage posts.<br/>
You can find details about fields of Post Schema on https://developer.wordpress.org/rest-api/reference/posts/#schema

#### Create post
```python3
from wordpresspy.utils import str_to_slug
from wordpresspy.wordpress import STATUS_PUBLISH

...

result = wpapi.create_post(
  author=0,
  content='Post full content',
  excerpt='Post description',
  slug=str_to_slug('Post slug of title'),
  status=STATUS_PUBLISH,
  title='Post Title'
)
print(result)
```

|Field      | Note                                                                |
|:----------|:--------------------------------------------------------------------|
|categories | Array of IDs (int). |
|date       | String with the following format: YYYY-MM-DD HH:MM:SS |
|tags       | Array of IDs (int). |

#### Update post
```python3
post_id = 110
result = wpapi.update_post(
    post_id,
    categories=[29],
    tags=[25],
    date='2018-01-26 00:00:00',
    title='Title changed',
    slug='new-slug',
    content='New content'
)
print(result)
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
posts = wpapi.get_posts()
print(posts)
```

Returns a list of [Post Schema](#post).

### Post revisions
The following methods helps you to manage post revisions.<br/>
You can find details about fields of Post Revisions Schema on https://developer.wordpress.org/rest-api/reference/post-revisions/#schema

#### Delete post revision
```python3
post_id = 89
revision_id = 95
wpapi.delete_post_revision(post_id, revision_id)
```

#### Get post revisions
```python3
post_id = 89
revisions = wpapi.get_post_revisions(post_id)
print(revisions)
```

### Tag
The following methods helps you to manage tags.<br/>
You can find details about fields of Tag Schema on https://developer.wordpress.org/rest-api/reference/tags/#schema

#### Create tag
```python3
from wordpresspy.utils import str_to_slug

...

result = wpapi.create_tag(
  description='Tag description',
  name='Tag title',
  slug=str_to_slug('Tag title'),
)
print(result)
```

#### Update tag
```python3
tag_id = 30
result = wpapi.update_tag(
  tag_id,
  name='New name'
)
print(result)
```

#### Delete tag
```python3
tag_id = 23
wpapi.delete_tag(tag_id)
```

#### Get tag
```python3
tag_id = 24
tag = wpapi.get_tag(tag_id)
print(tag)
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
