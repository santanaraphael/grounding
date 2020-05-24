import math
from typing import Tuple
from grounding.constants import HUMAM_BODY_RESISTANCE
from grounding.functions.get_tolerable_body_current_limit import get_tolerable_body_current_limit


def get_maximum_voltage_limits(
    shock_duration: float,
    ground_resistivity: float,
    insulating_layer_resistivity: float = 0,
    insulating_layer_thickness: float = 0,
    use_insulating_layer: bool = False,
    use_50kgs_model: bool = False,
) -> Tuple[float, float]:

    maximum_current = get_tolerable_body_current_limit(
        exposure_duration=shock_duration,
        use_50kgs_model=use_50kgs_model
    )

    if use_insulating_layer:
        insulation_correction_factor = 'foo' if use_insulating_layer else 1
        surface_material_resistivity = insulating_layer_resistivity
    else:
        insulation_correction_factor = 1
        surface_material_resistivity = ground_resistivity

    step_voltage = (
        HUMAM_BODY_RESISTANCE + 1.5 * insulation_correction_factor * surface_material_resistivity
    ) * maximum_current

    touch_voltage = (
        HUMAM_BODY_RESISTANCE + 1.5 * insulation_correction_factor * surface_material_resistivity
    ) * maximum_current

    return


def calc_max_values_50(trip_time, ground_ro, gravel_ro, gravel_depth):
    max_current = 0.116 / math.sqrt(trip_time)
    correction_factor = 1 - (0.09 * (1 - ground_ro / gravel_ro
                                     ) / (2 * gravel_depth + 0.09))

    max_touch_voltage = (1000 + 1.5 * correction_factor * gravel_ro) * max_current
    max_step_voltage = (1000 + 6 * correction_factor * gravel_ro) * max_current

    return max_touch_voltage, max_step_voltage
