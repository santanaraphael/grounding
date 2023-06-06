import math

from grounding.enums import SupportabilityConstant


def get_tolerable_body_current_limit(
    current_exposure_duration: float, supportability_constant: SupportabilityConstant
) -> float:
    """
    Equations (8) and (9) from the reference guide
    """
    if not 0.03 < current_exposure_duration < 3.0:
        raise ValueError("exposure_duration must be a value between 0.03s and 3.0s.")

    return supportability_constant.value / math.sqrt(current_exposure_duration)
