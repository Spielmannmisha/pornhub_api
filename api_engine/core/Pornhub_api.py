from typing import List
from urllib.request import urlopen
import urllib.parse
import json


class Pornhub_api:
    URL = "https://www.pornhub.com/webmasters"

    def make_url(self, path: str) -> str:
        """Concate base url with string from specific method"""
        return f"{self.URL}{path}"

    def __make_request(self, url, params=None):
        """Create full url with parameters

        Keyword arguments:
        url -- base url + category from specific method
        params -- dictionary with parameters that's been set by user

        Return:
        json as searching result with parameters
        """

        if params is not None:
            # Convert [params] dictionary to http query
            params = urllib.parse.urlencode(params)
            url = f"{url}?{params}"

        data = urlopen(url).read()  # Opens url via urllib.request library
        data = json.loads(data)  # Decoding json to a Python object [data]
        return data

    def search(
        self,
        q='',
        thumbsize='small',
        category=None,
        page=1,
        ordering=None,
        phrase: List[str] = None,
        tags: List[str] = None,
        period=None
            ):
        """Start searching with parameters

        Keyword arguments:
        q -- [string] user's query request. Default is ''.
        thumbsize -- [string] could be small, medium, large,
            small_hd, medium_hd, large_hd. Default is 'small'.
        category -- [string]. Default is None.
        page -- [int]. Default is 1
        ordering -- [string] could be featured, newest, mostviewed,
            rating. Defailt is None.
        phrase -- [List]. Default is None.
        tags -- [List]. Default is None.
        period -- [string]. Default is NOne

        Return:
        json as searching result with parameters
        """

        url = self.make_url('/search')

        # There we fill [params] dictionary
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
        """Check if video is active"""

        url = self.make_url('/is_video_active')

        params = {'id': id}

        data = self.__make_request(url, params)

        return data

    def categories(self):
        """Get all possible categories"""

        url = self.make_url('/categories')

        data = self.__make_request(url)

        return data

    def tags(self, tags: List[str] = None):
        """Get all tags"""
        url = self.make_url('/tags')
        params = None
        if tags is not None:
            params['tags'] = ','.join(tags)

        data = self.__make_request(url, params)

        return data
