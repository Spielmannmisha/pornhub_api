import json
import unittest
from unittest.mock import patch, Mock
from jsonschema import validate
from api_engine.core.pornhub_api import Pornhub_api
import os  # used to open filename path


def get_schema_response(func_name):
    """Get function name like /search and return both valid json schema
        and fake response.

    Keyword arguments:
    func_name -- [string] function name from pornhub_api.

    Return:
    schema -- [json] valid schema for specific func_name.
    response -- [json] full response for specific func_name.
    """

    def get_response_path(func_name):

        script_dir = os.path.dirname(__file__)
        rel_path = f"responses/{func_name}.json"
        abs_file_path = os.path.join(script_dir, rel_path)

        return abs_file_path

    def get_schema_path(func_name):

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

    @patch('api_engine.core.pornhub_api.Pornhub_api.make_request')
    def test_search(self, mock_search):

        schema, response = get_schema_response("search")

        mockfunc = Mock()
        mockfunc.urlopen.return_value = response

        mock_search.return_value = mockfunc.urlopen.return_value

        resp1 = Pornhub_api()
        resp = resp1.search('sex')

        self.assertIsInstance(resp, dict)
        self.assertTrue(resp)

        validate(resp, schema)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
