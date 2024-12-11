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

with open('intro.md') as f:
    intro = f.read()

with open('certifications.md') as f:
    certifications = f.read()

with open('links.md') as f:
    links = f.read()

feed_url = 'https://jimit105.medium.com/feed'
feed = feedparser.parse(feed_url)
print("Medium Feed Parsed")

articles = ''
for entry in feed.entries:
    articles += '<li><a href="' + entry.link + '">' + entry.title + '</a></li>'

medium = '<details open><summary><strong>:page_with_curl: Medium Articles</strong></summary><p><ul>' + \
    articles + '</ul></p></details>'


readme = '\n'.join([intro, medium, certifications, links])

with open('README.md', 'w') as f:
    f.write(readme)

print("README generated successfully")
