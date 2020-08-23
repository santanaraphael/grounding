
def get_insulation_correction_factor(
    ground_resistivity: float,
    insulating_layer_resistivity: float,
    insulating_layer_thickness: float,
) -> float:
    return 1 - (
        0.09 * (
            1 - ground_resistivity / insulating_layer_resistivity
        ) / (
            2 * insulating_layer_thickness + 0.09
        )
    )
