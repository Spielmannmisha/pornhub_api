import json
import unittest
from unittest.mock import patch, Mock
from jsonschema import validate
from api_engine.core.pornhub_api import Pornhub_api
import os  # used to open filename path


class TestGetData(unittest.TestCase):

    def setUp(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "schemas/search.json"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path) as d:
            schema = d.read()
        schema = json.loads(schema)
        self.valid_schema = schema

    @patch('api_engine.core.pornhub_api.Pornhub_api.make_request')
    def test_search(self, mock_search):

        script_dir = os.path.dirname(__file__)
        rel_path = "responses/search.json"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path) as d:
            example = d.read()
        example = json.loads(example)

        mockfunc = Mock()
        mockfunc.urlopen.return_value = example

        mock_search.return_value = mockfunc.urlopen.return_value

        resp1 = Pornhub_api()
        resp = resp1.search('sex')

        self.assertIsInstance(resp, dict)
        self.assertTrue(resp)
#        self.assertEqual(resp["rating"], "100")

        validate(resp, self.valid_schema)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
