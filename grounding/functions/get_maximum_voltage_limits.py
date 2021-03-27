import math
from typing import Tuple

from grounding.constants import HUMAM_BODY_RESISTANCE
from grounding.functions.get_insulation_correction_factor import (
    get_insulation_correction_factor,
)
from grounding.functions.get_tolerable_body_current_limit import (
    get_tolerable_body_current_limit,
)


def get_maximum_step_voltage(
    maximum_tolerable_current: float,
    insulation_correction_factor: float,
    surface_material_resistivity: float,
) -> float:
    return (
        HUMAM_BODY_RESISTANCE
        + 6.0 * insulation_correction_factor * surface_material_resistivity
    ) * maximum_tolerable_current


def get_maximum_touch_voltage(
    maximum_tolerable_current: float,
    insulation_correction_factor: float,
    surface_material_resistivity: float,
) -> float:
    return (
        HUMAM_BODY_RESISTANCE
        + 1.5 * insulation_correction_factor * surface_material_resistivity
    ) * maximum_tolerable_current


def get_maximum_voltage_limits(
    shock_duration: float,
    ground_resistivity: float,
    insulating_layer_resistivity: float = 0,
    insulating_layer_thickness: float = 0,
    use_50kgs_model: bool = False,
) -> Tuple[float, float]:

    maximum_tolerable_current = get_tolerable_body_current_limit(
        exposure_duration=shock_duration, use_50kgs_model=use_50kgs_model
    )

    if insulating_layer_resistivity and insulating_layer_thickness:

        insulation_correction_factor = get_insulation_correction_factor(
            ground_resistivity, insulating_layer_resistivity, insulating_layer_thickness
        )
        surface_material_resistivity = insulating_layer_resistivity
    else:

        insulation_correction_factor = 1.0
        surface_material_resistivity = ground_resistivity

    step_voltage = get_maximum_step_voltage(
        maximum_tolerable_current,
        insulation_correction_factor,
        surface_material_resistivity,
    )

    touch_voltage = get_maximum_touch_voltage(
        maximum_tolerable_current,
        insulation_correction_factor,
        surface_material_resistivity,
    )

    return step_voltage, touch_voltage
