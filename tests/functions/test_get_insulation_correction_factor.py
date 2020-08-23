from unittest import TestCase
from grounding.functions.get_insulation_correction_factor import get_insulation_correction_factor


class GetInsulationCorrectionFactorTest(TestCase):

    def test_sample_from_textbook(self):
        insulation_correction_factor = get_insulation_correction_factor(
            ground_resistivity=400,
            insulating_layer_resistivity=2500,
            insulating_layer_thickness=0.102
        )

        self.assertAlmostEqual(insulation_correction_factor, 0.74, 2)
