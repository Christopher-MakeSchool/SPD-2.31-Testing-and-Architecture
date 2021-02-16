# By Kami Bigdely
# Remove assignment to method parameter.


class Distance:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value


class Mass:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit


def incorrect_unit():
    return (distance.unit != 'km') or (mass.unit != 'kg')


def calculate_kinetic_energy(mass, distance, time):
    KM_CONST = 9.461e12
    KG_CONST = 1.98892e30

    if incorrect_unit():
        # [ly] stands for light-year (measure of distance in astronomy)
        if distance.unit == "ly":
            # convert from light-year to km unit
            km_distance = Distance(distance.value * KM_CONST, "km")
        if mass.unit == "solar-mass":
            # convert from solar mass to kg
            kg_mass = Mass(mass.value * KG_CONST, 'kg')
    else:
        print("unit is Unknown")
        return

    speed = km_distance.value/time  # [km per sec]
    kinetic_energy = 0.5 * kg_mass.value * speed ** 2
    return kinetic_energy


if __name__ == "__main__":
    mass = Mass(2, "solar-mass")
    distance = Distance(2, 'ly')
    print(calculate_kinetic_energy(mass, distance, 3600e20))
