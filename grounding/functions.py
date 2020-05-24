

def calculate_max_voltages(
    trip_time: float,
    ground_resistivity: float,
    insulation_resistivity: float,
    insulation_depth: float,
    use_50kgs: bool = False,
) -> Tuple[float, float]:
    if use_50kgs:
        supportability_constant = 0.116
    else:
        supportability_constant = 0.157

    return ''


def calc_max_values_50(trip_time, ground_ro, gravel_ro, gravel_depth):
    max_current = 0.116 / math.sqrt(trip_time)
    correction_factor = 1 - (0.09 * (1 - ground_ro / gravel_ro
                                     ) / (2 * gravel_depth + 0.09))

    max_touch_voltage = (1000 + 1.5 * correction_factor * gravel_ro) * max_current
    max_step_voltage = (1000 + 6 * correction_factor * gravel_ro) * max_current

    return max_touch_voltage, max_step_voltage


def calc_max_values_70(trip_time, ground_ro, gravel_ro, gravel_depth):
    max_current = 0.157 / math.sqrt(trip_time)
    correction_factor = 1 - (0.09 * (1 - ground_ro / gravel_ro
                                     ) / (2 * gravel_depth + 0.09))

    max_touch_voltage = (1000 + 1.5 * correction_factor * gravel_ro) * max_current
    max_step_voltage = (1000 + 6 * correction_factor * gravel_ro) * max_current

    return max_touch_voltage, max_step_voltage
