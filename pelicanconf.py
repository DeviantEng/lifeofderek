#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Derek Horn'
SITENAME = u'Life of Derek'
SITEURL = 'http://lifeofderek.com'
TIMEZONE = 'America/Kentucky/Louisville'
THEME = './theme/bootstrap3'
BOOTSTRAP_THEME = 'readable'
SUMMARY_MAX_LENGTH = 50
FAVICON = 'images/favicon.png'
DISQUS_SITENAME = "lifeofderek"
GOOGLE_ANALYTICS = "UA-52148643-1"

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
CATEGORY = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
DISPLAY_TAGS_INLINE = 'True'

DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'misc'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d %b %Y'
DEFAULT_PAGINATION = False

LINKS = (('Deviant Engineer', 'http://DeviantEngineer.com'),
         ('Custom IT Solutions', 'http://Custom-ITS.com'),
         )

SOCIAL = (('Facebook', 'http://facebook.com/tycoonbob'),
          ('twitter', 'http://twitter.com/DeviantEng'),
          ('linkedin', 'http://www.linkedin.com/in/hornd'),
          ('github', 'http://github.com/DeviantEng'),
          )
          
PLUGIN_PATHS  = ['./plugins',
]
PLUGINS = ['feed_summary', 'gzip_cache', 'liquid_tags.video', 'optimize_images', 'related_posts', 'share_post', 'sitemap',]

FEED_USE_SUMMARY = True
STATIC_PATHS = ['images', 'videos', 'extra']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},}
RELATED_POSTS_MAX = 3
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
