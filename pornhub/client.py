from typing import List
from urllib.request import urlopen
import urllib.parse
import json


class PornhubApi:
    """This class creates functions that interact with pornhub.com

    Returns:
        functions: returns different api functions that interact with pornhub
    """

    URL = "https://www.pornhub.com/webmasters"

    def make_url(self, path: str) -> str:
        """Concate base url with string from specific method"""
        return f"{self.URL}{path}"

    def make_request(self, url, params=None):
        """this function makes api request to pornhub

        Args:
            url (String): unique url for each method
            params (List, optional): search parameters. Defaults to None.

        Returns:
            json: returns json that depends on parameters
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

        Args:
            q (str, optional): [description]. Defaults to ''.
            thumbsize (str, optional): [description]. Defaults to 'small'.
            category ([type], optional): [description]. Defaults to None.
            page (int, optional): [description]. Defaults to 1.
            ordering ([type], optional): [description]. Defaults to None.
            phrase (List[str], optional): [description]. Defaults to None.
            tags (List[str], optional): [description]. Defaults to None.
            period ([type], optional): [description]. Defaults to None.

        Returns:
            json: returns json as searching result with parameters
        """

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
        data = self.make_request(url, params)
        return data

    def stars(self):
        """Get short pornstars list"""

        url = self.make_url('/stars')
        data = self.make_request(url)
        return data

    def stars_detailed(self):
        """Get detailed pornstars list"""

        url = self.make_url('/stars_detailed')
        data = self.make_request(url)
        return data

    def video_by_id(self, id):
        """Get video id"""

        url = self.make_url('/video_by_id')
        params = {'id': id}
        data = self.make_request(url, params)
        return data

    def is_video_active(self, id):
        """Check if video is active"""

        url = self.make_url('/is_video_active')
        params = {'id': id}
        data = self.make_request(url, params)
        return data

    def categories(self):
        """Get all possible categories"""

        url = self.make_url('/categories')
        data = self.make_request(url)
        return data

    def tags(self, tags: List[str] = None):
        """Get all tags"""

        url = self.make_url('/tags')
        params = None
        if tags is not None:
            params['tags'] = ','.join(tags)
        data = self.make_request(url, params)
        return data
