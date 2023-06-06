from unittest import TestCase

from grounding.enums import SupportabilityConstant
from grounding.functions.get_tolerable_body_current_limit import (
    get_tolerable_body_current_limit,
)


class GetTolerableBodyCurrentLimitTest(TestCase):
    def test_sample_from_textbook(self):
        exposure_time = 0.5
        current_limit = get_tolerable_body_current_limit(
            exposure_time, supportability_constant=SupportabilityConstant.FOR_70_KGS
        )
        self.assertAlmostEqual(current_limit, 0.2220315292925759)

    def test_sample_from_textbook_with_50kgs(self):
        exposure_time = 0.5
        current_limit = get_tolerable_body_current_limit(
            exposure_time, supportability_constant=SupportabilityConstant.FOR_50_KGS
        )
        self.assertAlmostEqual(current_limit, 0.16404877323527903)

    def test_small_exposure_time(self):
        with self.assertRaises(ValueError):
            current_limit = get_tolerable_body_current_limit(
                0.029, SupportabilityConstant.FOR_70_KGS
            )
            self.assertIsNone(current_limit)

    def test_large_exposure_time(self):
        with self.assertRaises(ValueError):
            current_limit = get_tolerable_body_current_limit(
                3.1, SupportabilityConstant.FOR_70_KGS
            )
            self.assertIsNone(current_limit)
