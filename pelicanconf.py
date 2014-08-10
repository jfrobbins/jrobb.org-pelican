#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jon Robbins'
SITENAME = u'jrobb.org'
SITEURL = 'http://jrobb.org'

THEME = '../pelican-themes/bootstrap2'
#THEME = '../pelican-themes/foundation-default-colours'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED = 'feeds/all.atom.xml'
FEED_DOMAIN = SITEURL
TRANSLATION_FEED_ATOM = None
FEED_ALL_ATOM = None
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
#AUTHOR_FEED_ATOM = 'feeds/%s.atom.xml'

# Feeds 
FEEDS =  (('All posts', 'feeds/all.atom.xml'),
          ('Category', 'feeds/category'),
         )

# Blogroll
LINKS = (('my GMG', 'https://media.jrobb.org/'),
         ('hastebin', 'http://bin.jrobb.org/'),
         ('pump.io', 'https://io.jrobb.org/'),
        )

# Social widget
SOCIAL = (
          ('pump.io', 'https://io.jrobb.org'),
          ('@jrobb', 'https://quitter.se/jrobb'),
          ('g+', 'https://plus.google.com/+JonathanRobbinsNC/'),
          ('@jrobbnc', 'https://twitter.com/jrobbnc'),
          )

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
