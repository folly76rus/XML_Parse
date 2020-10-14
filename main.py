# -*- coding: utf-8 -*-

import xml.etree.ElementTree as et
import requests
from pprint import pprint


def parse_xml_url(url):
    pass


url = 'http://rustattoo.ru/system/tattoo-rss.xml'
root = et.fromstring(requests.get(url).content.decode('utf-8'))
items = root.iter('item')
result = [[item.find('enclosure').get('url'), item.find('link').text, item.find('title').text] for item in root.iter('item')]
pprint(result)

