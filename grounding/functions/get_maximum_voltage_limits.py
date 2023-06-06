from typing import Tuple

from grounding.constants import HUMAN_BODY_RESISTANCE
from grounding.enums import SupportabilityConstant
from grounding.functions.get_insulation_correction_factor import (
    get_insulation_correction_factor,
)
from grounding.functions.get_tolerable_body_current_limit import (
    get_tolerable_body_current_limit,
)


def get_maximum_step_voltage(
    tolerable_body_current_limit: float,
    insulation_correction_factor: float,
    surface_material_resistivity: float,
) -> float:
    """
    Equations (29) and (30) from the reference guide
    """
    return (
        HUMAN_BODY_RESISTANCE
        + 6.0 * insulation_correction_factor * surface_material_resistivity
    ) * tolerable_body_current_limit


def get_maximum_touch_voltage(
    tolerable_body_current_limit: float,
    insulation_correction_factor: float,
    surface_material_resistivity: float,
) -> float:
    """
    Equations (32) and (33) from the reference guide
    """
    return (
        HUMAN_BODY_RESISTANCE
        + 1.5 * insulation_correction_factor * surface_material_resistivity
    ) * tolerable_body_current_limit


def get_maximum_voltage_limits(
    current_expose_duration: float,
    ground_resistivity: float,
    insulation_layer_resistivity: float = 0,
    insulation_layer_thickness: float = 0,
    supportability_constant: SupportabilityConstant = SupportabilityConstant.FOR_70_KGS,
) -> Tuple[float, float]:

    tolerable_body_current_limit = get_tolerable_body_current_limit(
        current_exposure_duration=current_expose_duration,
        supportability_constant=supportability_constant,
    )

    if insulation_layer_resistivity and insulation_layer_thickness:

        insulation_correction_factor = get_insulation_correction_factor(
            ground_resistivity, insulation_layer_resistivity, insulation_layer_thickness
        )
        surface_material_resistivity = insulation_layer_resistivity
    else:
        insulation_correction_factor = 1.0
        surface_material_resistivity = ground_resistivity

    step_voltage = get_maximum_step_voltage(
        tolerable_body_current_limit,
        insulation_correction_factor,
        surface_material_resistivity,
    )

    touch_voltage = get_maximum_touch_voltage(
        tolerable_body_current_limit,
        insulation_correction_factor,
        surface_material_resistivity,
    )

    return step_voltage, touch_voltage
