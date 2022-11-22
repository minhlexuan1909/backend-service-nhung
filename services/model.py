LIGHT_THRESHOLD = 2000
HUMIDITY_THRESHOLD = 700

def can_turn_on_pump(humidity: float):
    return humidity >= HUMIDITY_THRESHOLD


def can_turn_on_light(light: float):
    return light >= LIGHT_THRESHOLD
