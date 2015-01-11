#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kathy Lin'
SITENAME = u'Kathy Lin'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/kathyl'),
          ('LinkedIn', 'https://www.linkedin.com/pub/kathy-lin/54/932/50'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True

# Theme
# THEME = 'themes/built-texts'
THEME = '../themes/foundation-default-colours'
# THEME = 'themes/gum'
# THEME = 'themes/pelican-bootstrap3'
# THEME = 'themes/simple-bootstrap'

STATIC_PATHS = [
    'content/extra/CNAME',
    ]
EXTRA_PATH_METADATA = {
    'content/extra/CNAME': {'path': 'CNAME'},
    }