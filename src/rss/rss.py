import requests
from requests.exceptions import Timeout, HTTPError
import traceback
import xml.etree.ElementTree as ET
from email.utils import parsedate
from time import mktime


class RssAPI:
    def __init__(self):
        self.RSS_PATH = 'https://www.fukuishimbun.co.jp/list/feed/rss'

    def fetch_rss(self):

        try:
            r = requests.get(self.RSS_PATH, timeout=(3.0, 7.5))
            r.raise_for_status()
            parsed_xml = [
                {j.tag: j.text for j in i}
                for i in ET.fromstring(r.text).findall('./channel/item')
            ]
            return [self.__convert_to_dict(doc) for doc in parsed_xml]

        except Timeout:
            print(traceback.print_exc())
        except HTTPError:
            print(traceback.print_exc())

        return []

    def __convert_to_dict(self, doc):
        return {
            'link': doc['link'],
            'title': doc['title'],
            'published_at': mktime(parsedate(doc['pubDate']))
        }
