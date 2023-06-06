from unittest import TestCase

from grounding.functions.get_maximum_voltage_limits import (
    get_maximum_step_voltage,
    get_maximum_touch_voltage,
    get_maximum_voltage_limits,
)


class GetVoltageLimitsTest(TestCase):
    def test_step_limit_example(self):
        maximum_step_voltage = get_maximum_step_voltage(
            tolerable_body_current_limit=0.2220315292925759,
            insulation_correction_factor=0.74,
            surface_material_resistivity=2500,
        )

        self.assertAlmostEqual(maximum_step_voltage, 2686.6, 1)

    def test_touch_limit_example(self):
        maximum_touch_voltage = get_maximum_touch_voltage(
            tolerable_body_current_limit=0.2220315292925759,
            insulation_correction_factor=0.74,
            surface_material_resistivity=2500,
        )

        self.assertAlmostEqual(maximum_touch_voltage, 838.2, 1)

    def test_both_voltages_example(self):
        maximum_step_voltage, maximum_touch_voltage = get_maximum_voltage_limits(
            current_expose_duration=0.5,
            ground_resistivity=400,
            insulation_layer_resistivity=2500,
            insulation_layer_thickness=0.102,
        )

        self.assertAlmostEqual(maximum_step_voltage, 2686.6, delta=20)
        self.assertAlmostEqual(maximum_touch_voltage, 838.2, delta=20)
