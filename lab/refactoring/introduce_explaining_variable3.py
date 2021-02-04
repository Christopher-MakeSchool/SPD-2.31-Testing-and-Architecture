# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05


def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    _current_state = time * temperature * pressure * COOKED_CONSTANT
    is_well_done = _current_state >= WELL_DONE
    is_medium = _current_state >= MEDIUM
    return (is_well_done and desired_state == 'well-done') or (is_medium and desired_state == 'medium')
