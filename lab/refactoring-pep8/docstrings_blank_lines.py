# by Kami Bigdely
# Docstrings and blank lines


class OnBoardTemperatureSensor:
    """Return the detected Temperature in celcius from the onboard sensors."""

    VOLTAGE_TO_TEMP_FACTOR = 5.6

    def __init__(self):
        """Initalize the class with any presets or give paramaters."""
        pass

    def read_voltage(self):
        """Read the voltage value from our sensor."""
        # In real life, it should read from hardware.
        return 2.7

    def get_temperature(self):
        """Convert the voltage value to a tempurature"""
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR  # [celcius]


class CarbonMonoxideSensor:
    """Return the detected Carbon Monoxide from the onboard sensors."""

    VOLTAGE_TO_CO_FACTOR = 0.048

    def __init__(self, temperature_sensor):
        """Initalize the class with the given temperature sensor otherwise create a new sensor."""
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()

    def get_carbon_monoxide_level(self):
        """Return the carbon monoxide level calculated from our sensor."""
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(
            sensor_voltage, self.on_board_temp_sensor.get_temperature())
        return self.carbon_monoxide

    def read_sensor_voltage(self):
        """Return the voltage read from a sensor."""
        # In real life, it should read from hardware.
        return 2.3

    def convert_voltage_to_carbon_monoxide_level(self, voltage, temperature):
        """Convert & return a given voltage to a carbonmonoxide level."""
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature


class DisplayUnit:
    """Returns a display message."""

    def __init__(self):
        """Initalize the class with the given string."""
        self.string = ''

    def display(self, msg):
        """Prints a message from our sensor to the console."""
        print(msg)


class CarbonMonoxideDevice():
    """Sends a display message with the calculated Carbon Monoxide from the sensors."""

    def __init__(self, co_sensor, display_unit):
        """Initalize the class with the given CarbonMonoxide Sensor and Display Unit."""
        self.carbonMonoxideSensor = co_sensor
        self.display_unit = display_unit

    def Display(self):
        """Craft a message to display with our connected display unit."""
        msg = 'Carbon Monoxide Level is : ' + \
            str(self.carbonMonoxideSensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)


if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.Display()
