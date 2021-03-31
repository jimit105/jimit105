# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:56:00 2020

@author: Jimit.Dholakia
"""


import feedparser
import time
import urllib.parse
import os

os.environ['TZ'] = 'Asia/Kolkata'
time.tzset()

#updated  ='Last Updated on: ' + time.strftime('%b %d, %Y %X %Z', time.localtime())
current_time = time.strftime('%b %d, %Y %X %Z', time.localtime())
# updated = '![Last Updated](https://img.shields.io/badge/Last%20Updated%20on-' + \
#    urllib.parse.quote(current_time) + '-brightgreen)'

with open('intro.md') as f:
    intro = f.read()

# intro += updated

with open('certifications.md') as f:
    certifications = f.read()

with open('links.md') as f:
    links = f.read()

feed_url = 'https://medium.com/feed/@jimit105'
feed = feedparser.parse(feed_url)

articles = ''
for entry in feed.entries:
    articles += '<li><a href="' + entry.link + '">' + entry.title + '</a></li>'

medium = '<details open><summary><strong>:page_with_curl: Medium Articles</strong></summary><p><ul>' + \
    articles + '</ul></p></details>'


readme = '\n'.join([intro, certifications, medium, links])

with open('README.md', 'w') as f:
    f.write(readme)
