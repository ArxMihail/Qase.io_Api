"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import qaseio
from qaseio.api.search_api import SearchApi  # noqa: E501


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self):
        self.api = SearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_search(self):
        """Test case for search

        Search entities by Qase Query Language (QQL).  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
