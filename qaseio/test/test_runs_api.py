"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import qaseio
from qaseio.api.runs_api import RunsApi  # noqa: E501


class TestRunsApi(unittest.TestCase):
    """RunsApi unit test stubs"""

    def setUp(self):
        self.api = RunsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_complete_run(self):
        """Test case for complete_run

        Complete a specific run.  # noqa: E501
        """
        pass

    def test_create_run(self):
        """Test case for create_run

        Create a new run.  # noqa: E501
        """
        pass

    def test_delete_run(self):
        """Test case for delete_run

        Delete run.  # noqa: E501
        """
        pass

    def test_get_run(self):
        """Test case for get_run

        Get a specific run.  # noqa: E501
        """
        pass

    def test_get_runs(self):
        """Test case for get_runs

        Get all runs.  # noqa: E501
        """
        pass

    def test_update_run_publicity(self):
        """Test case for update_run_publicity

        Update publicity of a specific run.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
