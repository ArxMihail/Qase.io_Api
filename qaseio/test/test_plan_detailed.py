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
from qaseio.model.plan import Plan
from qaseio.model.plan_detailed_all_of import PlanDetailedAllOf
from qaseio.model.plan_detailed_all_of_cases import PlanDetailedAllOfCases
globals()['Plan'] = Plan
globals()['PlanDetailedAllOf'] = PlanDetailedAllOf
globals()['PlanDetailedAllOfCases'] = PlanDetailedAllOfCases
from qaseio.model.plan_detailed import PlanDetailed


class TestPlanDetailed(unittest.TestCase):
    """PlanDetailed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPlanDetailed(self):
        """Test PlanDetailed"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PlanDetailed()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()