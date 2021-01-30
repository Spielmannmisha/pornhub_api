from typing import List, Optional
from urllib.request import Request, urlopen
import urllib.parse 
import json


class WebUrlBuilder:
    
    URL = "https://www.pornhub.com/webmasters"

    def make_url(self, path: str) -> str:
        return f"{self.URL}{path}"
    
    def make_request(self, params):
        """To delete"""
        urlreq = Request(url)
        content = urlopen(urlreq).read()
        data = json.loads(content)
        return data

    def search(
        self,
        q = '',
        thumbsize = 'small',
        category = '',
        page = 1,
        ordering = '',
        phrase = '',
        tags = '',
        period = '' 
        ):
        url = self.make_url('/search')
                
        params = {'search': q, 'page': page, 'thumbsize': thumbsize}

        if category is not None:
            params['category'] = category
        if ordering is not None:
            params['ordering'] = ordering
        if phrase is not None:
            params['phrase'] = ','.join(phrase)
        if tags is not None:
            params['tags'] = ','.join(tags)
        if period is not None and category is not None:
            params['period'] = period

        data = urllib.parse.urlencode(params)
        data = data.encode('ascii')
        urlreq = Request(url, data)

        content = urlopen(urlreq).read()
        output = json.loads(content)

        return data


    def stars(self):
        url = self.make_url('/stars')
        return url

    def tags(self, *args):
        url = self.make_url('/tags')


    def stars(self):
        url = self.make_url('/stars')
        return url


    def video_by_id(self):
        url = self.make_url('/vide_by_id')
        return



"""
with open('test.txt', 'w', encoding= 'utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent = 4)
"""

test = WebUrlBuilder()

print(test.search(q = 'Anal'))