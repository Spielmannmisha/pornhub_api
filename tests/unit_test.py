import json
import unittest
from unittest.mock import patch, Mock
from pornhub.client import PornhubApi
import os


def get_schema_response(func_name):
    """Get function name like /search and return both valid json schema
        and fake response.

    Args:
        func_name (String): function name that will be used in path
    """

    def get_response_path(func_name):
        """This function creates path for response example depending on func_name

        Args:
            func_name (String): function name that will be used in path

        Returns:
            String: full path of response example
        """

        script_dir = os.path.dirname(__file__)
        rel_path = f"responses/{func_name}.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        return abs_file_path

    def get_schema_path(func_name):
        """This function creates path for json schema depending on func_name

        Args:
            func_name (String): function name that will be used in path

        Returns:
            String: full path of json schema
        """

        script_dir = os.path.dirname(__file__)
        rel_path = f"schemas/{func_name}.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        return abs_file_path

    def open_file(input):
        with open(input) as a:
            data = a.read()
        data = json.loads(data)
        return data

    schema = open_file(get_schema_path(func_name))
    response = open_file(get_response_path(func_name))
    return schema, response


class TestGetData(unittest.TestCase):
    @patch("pornhub.client.PornhubApi.make_request")
    def test_search(self, mock_search):
        schema, response = get_schema_response("search")
        response = json.dumps(response)
        mockfunc = Mock()
        mockfunc.r.content.return_value = response
        mock_search.return_value = mockfunc.r.content.return_value

        resp = PornhubApi()
        resp = resp.search("sex")
        self.assertIsInstance(resp, list)
        self.assertTrue(resp)
        self.assertEqual(resp, schema)

    @patch("pornhub.client.PornhubApi.make_request")
    def test_stars(self, mock_stars):
        schema, response = get_schema_response("stars")
        response = json.dumps(response)
        mockfunc = Mock()
        mockfunc.r.content.return_value = response
        mock_stars.return_value = mockfunc.r.content.return_value

        resp = PornhubApi()
        resp = resp.stars()
        self.assertIsInstance(resp, list)
        self.assertTrue(resp)
        self.assertEqual(resp, schema)

    @patch("pornhub.client.PornhubApi.make_request")
    def test_stars_detailed(self, mock_stars_detailed):
        schema, response = get_schema_response("stars_detailed")
        response = json.dumps(response)
        mockfunc = Mock()
        mockfunc.r.content.return_value = response
        mock_stars_detailed.return_value = mockfunc.r.content.return_value

        resp = PornhubApi()
        resp = resp.stars_detailed()
        self.assertIsInstance(resp, list)
        self.assertTrue(resp)
        self.assertEqual(resp, schema)

    @patch("pornhub.client.PornhubApi.make_request")
    def test_video_by_id(self, mock_video_by_id):
        schema, response = get_schema_response("video_by_id")
        response = json.dumps(response)
        mockfunc = Mock()
        mockfunc.r.content.return_value = response
        mock_video_by_id.return_value = mockfunc.r.content.return_value

        resp = PornhubApi()
        resp = resp.video_by_id(id="id123445")
        self.assertIsInstance(resp, dict)
        self.assertTrue(resp)
        self.assertEqual(resp, schema)

    @patch("pornhub.client.PornhubApi.make_request")
    def test_is_video_active(self, mock_is_video_active):
        schema, response = get_schema_response("is_video_active")
        response = json.dumps(response)
        mockfunc = Mock()
        mockfunc.r.content.return_value = response
        mock_is_video_active.return_value = mockfunc.r.content.return_value

        resp = PornhubApi()
        resp = resp.is_video_active(id="id12344")
        self.assertIsInstance(resp, dict)
        self.assertTrue(resp)
        self.assertEqual(resp, schema)

    @patch("pornhub.client.PornhubApi.make_request")
    def test_categories(self, mock_categories):
        schema, response = get_schema_response("categories")
        response = json.dumps(response)
        mockfunc = Mock()
        mockfunc.r.content.return_value = response
        mock_categories.return_value = mockfunc.r.content.return_value

        resp = PornhubApi()
        resp = resp.categories()
        self.assertIsInstance(resp, list)
        self.assertTrue(resp)
        self.assertEqual(resp, schema)

    @patch("pornhub.client.PornhubApi.make_request")
    def test_tags(self, mock_tags):
        schema, response = get_schema_response("tags")
        response = json.dumps(response)
        mockfunc = Mock()
        mockfunc.r.content.return_value = response
        mock_tags.return_value = mockfunc.r.content.return_value

        resp = PornhubApi()
        resp = resp.tags()
        self.assertIsInstance(resp, list)
        self.assertTrue(resp)
        self.assertEqual(resp, schema)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
