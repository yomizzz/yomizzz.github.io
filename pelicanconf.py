#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'yomi'
SITENAME = 'Yomi blog'
SITESUBTITLE = 'A personal blog.'
SITEURL = 'https://yomizzz.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'cn'

GITHUB_URL = 'https://github.com/yomizzz/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Notion', 'https://y0m1.notion.site/yomi-aa1b6d79b81b4319b48dd6d465f95c4c'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/yomizzz/'),
          )

DEFAULT_PAGINATION = False
DEFAULT_DATE_FORMAT = '%Y %b %d %A'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Articles'

# DISPLAY_PAGES_ON_MENU = True
# DISPLAY_CATEGORIES_ON_MENU = True
# PLUGIN_PATHS = ["/Users/yomi/Blog/pelican-plugins", ]
# PLUGINS = ["sitemap", ]
'''
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}
'''
STATIC_PATHS = ['extra/robots.txt', 'extra/sitemap.xml', ]
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'}, 'extra/sitemap.xml': {'path': 'sitemap.xml'},}

