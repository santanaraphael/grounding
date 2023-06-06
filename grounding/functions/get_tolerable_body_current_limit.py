import math

from grounding.enums import SupportabilityConstant


def get_tolerable_body_current_limit(
    exposure_duration: float,
    use_50kgs_model: bool = False,
) -> float:

    if not 0.03 < exposure_duration < 3.0:
        raise ValueError("exposure_duration must be a value between 0.03s and 3.0s.")

    if use_50kgs_model:
        body_weight_constant = SupportabilityConstant.USE_50_KGS.value
    else:
        body_weight_constant = SupportabilityConstant.USE_70_KGS.value

    return body_weight_constant / math.sqrt(exposure_duration)
