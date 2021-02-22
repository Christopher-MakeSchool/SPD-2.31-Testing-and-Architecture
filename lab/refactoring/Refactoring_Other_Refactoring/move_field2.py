# Kami Bigdely
# Move Field


class Cabin:
    def __init__(self):
        pass


class Engine:
    def __init__(self):
        pass


class FuelTank:
    def __init__(self):
        pass


class Tpms:
    """Tire Pressure Monitoring System."""

    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.sensor_transmit_range = 300        # [feet]
        self.sensor_pressure_range = (8, 300)   # [PSI]
        self.battery_life = 6                   # [year]

    def get_pressure(self):
        return 3

    def get_serial_number(self):
        return self.serial_number


class Wheel:
    def __init__(self, wheel_location=None, pressure_monitor=None):
        self.wheel_location = wheel_location
        self.pressure_monitor = pressure_monitor

    def install_tire(self):
        print('remove old tube.')
        print('cleaned tpms: ', self.pressure_monitor.get_serial_number, '.')
        print('installed new tube.')

    def read_tire_pressure(self):
        return self.pressure_monitor.get_pressure()

    def set_car(self, car):
        self.car = car


class Car:
    def __init__(self, cabin, engine, fuel_tank, wheels):
        self.cabin = cabin
        self.fuel_tank = fuel_tank
        self.engine = engine
        self.wheels = wheels
        # Set wheels' car reference into each wheel.
        for w in wheels:
            w.set_car(self)


if __name__ == "__main__":
    cabin = Cabin()
    engine = Engine()
    fuel_tank = FuelTank()

    wheels = [
        Wheel('front-left', Tpms(4343083)),
        Wheel('front-right', Tpms(983408543)),
        Wheel('back-left', Tpms(3498857)),
        Wheel('back-right', Tpms(23654835))
    ]

    my_car = Car(cabin, engine, fuel_tank, wheels)
