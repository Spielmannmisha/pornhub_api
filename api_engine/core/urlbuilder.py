from typing import List, Optional
from urllib.request import Request, urlopen
import urllib.parse 
import json


class WebUrlBuilder:
    
    URL = "https://www.pornhub.com/webmasters"

    def make_url(self, path: str) -> str:
        return f"{self.URL}{path}"

    def __make_request(self, url, params = None):
        """Create full url with parameters
        Returns json with searching result with parameters 
        """
               
       # data = urllib.parse.urlencode(params)

        if params is not None:
            params = urllib.parse.urlencode(params) #Convert [params] dictionary to http query
            url = f"{url}?{params}"

        data = urlopen(url).read()  #Opens url via urllib.request library
        data = json.loads(data)  #Decoding json to a Python object [data]
        return data

    def search(
        self,
        q = '',
        thumbsize = 'small',
        category = None,
        page = 1,
        ordering = None,
        phrase: List[str] = None,
        tags: List[str] = None,
        period = None 
        ):
        """Start searching with parameters
        
            Returns json with searching result with parameters"""

        url = self.make_url('/search')

        #There we fill [params] dictionary
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

        data = self.__make_request(url, params)

        return data

    def stars(self):
        """Get short pornstars list"""

        url = self.make_url('/stars')

        data = self.__make_request(url)

        return data

    def stars_detailed(self):
        """Get detailed pornstars list"""

        url = self.make_url('/stars_detailed')

        data = self.__make_request(url)

        return data

    def video_by_id(self, id):
        """Get video id"""

        url = self.make_url('/video_by_id')

        params = {'id': id}

        data = self.__make_request(url, params)

        return data

    def is_video_active(self, id):
    
        url = self.make_url('/is_video_active')

        params = {'id': id}

        data = self.__make_request(url, params)

        return data

    def categories(self):
        
        url = self.make_url('/categories')

        data = self.__make_request(url)

        return data 

    def tags(self, tags: List[str] = None):
        
        url = self.make_url('/tags')

        if tags is not None:
            params['tags'] = ','.join(tags)

        data = self.__make_request(url, params)

        return data