import numpy as np

center = (-75.12601884604852, 39.95066669151871)
radius = 0.001

def fly(time_s: float) -> tuple[float, float]:
    """fly the drone to the designated point in time
    """
    return (center[0] + radius * np.cos(time_s), center[1] + radius * np.sin(time_s))

