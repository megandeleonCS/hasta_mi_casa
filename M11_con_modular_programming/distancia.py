"""
distance.py - Mathematical calculations for geographic distances.
"""

import math


def calcular_haversine(lat1, lon1, lat2, lon2, unidad="km"):
    """
    Calculates great-circle distance between two points (as the bird flies).
    (Placeholder ready for implementation in M12).
    """
    # Earth radius
    r = 6371.0 if unidad == "km" else 3958.8

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return round(r * c, 2)