"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qaseio
from qaseio.model.attachment import Attachment
from qaseio.model.test_step_result import TestStepResult
globals()['Attachment'] = Attachment
globals()['TestStepResult'] = TestStepResult
from qaseio.model.result import Result


class TestResult(unittest.TestCase):
    """Result unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResult(self):
        """Test Result"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Result()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
