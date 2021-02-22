# by Kami Bigdely
# Extract class


WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05


def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    _current_state = time * temperature * pressure * COOKED_CONSTANT
    is_well_done = _current_state >= WELL_DONE
    is_medium = _current_state >= MEDIUM
    return (is_well_done and desired_state == 'well-done') or (is_medium and desired_state == 'medium')


if __name__ == "__main__":
    time = 30  # [min]
    temp = 103  # [celcius]
    pressure = 20  # [psi]
    desired_state = 'well-done'

    if is_cookeding_criteria_satisfied(time, temp, pressure, desired_state):
        print('cooking is done.')
    else:
        print('ongoing cooking.')
