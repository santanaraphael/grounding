def get_insulation_correction_factor(
    ground_resistivity: float,
    insulation_layer_resistivity: float,
    insulation_layer_thickness: float,
) -> float:
    """
    Equation (27) from the reference guide
    """
    return 1 - (
        0.09
        * (1 - ground_resistivity / insulation_layer_resistivity)
        / (2 * insulation_layer_thickness + 0.09)
    )
