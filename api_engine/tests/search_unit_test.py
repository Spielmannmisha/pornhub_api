import unittest
from unittest.mock import patch, Mock
from jsonschema import validate
from api_engine.core.pornhub_api import Pornhub_api


class TestGetData(unittest.TestCase):

    def setUp(self):

        self.valid_schema = {
            "type": "object",
            "properties": {
                "duration": {"type": "number"},
                "views": {"type": "number"},
                "video_id": {"type": "string"},
                "rating": {"type": "string"}
            },
            "required": ["duration", "views", "video_id", "rating"]
        }

    @patch('api_engine.core.pornhub_api.Pornhub_api.make_request')
    def test_search(self, mock_search):

        mockfunc = Mock()
        mockfunc.urlopen.return_value = {
            "duration": 1,
            "views": 1,
            "video_id": "ph5eee6649f7ee",
            "rating": "100"
        }

        mock_search.return_value = mockfunc.urlopen.return_value

        resp1 = Pornhub_api()
        resp = resp1.search('sex')

        self.assertIsInstance(resp, dict)
        self.assertTrue(resp)
        self.assertEqual(resp["rating"], "100")

        validate(resp, self.valid_schema)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
