class Subject:
    """Represents what is being observed"""

    def __init__(self):
        """create an empty observer list"""
        self._observers = []

    # This method is called to notify all observers
    # when the Subject's state (measurements) has changed.
    def notify(self, modifier=None):
        """Alert the observers"""
        # We notify the observers when we get updated measurements
        # from the Weather Station.
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    # Both of the following two methods take an observer as an argument;
    # That is, the observer to be registered or removed.
    def attach(self, observer):
        """If the observer is not in the list, append it into the list"""
        # When an observer registers, we just
        # add it to the end of the list.
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """Remove the observer from the observer list"""
        # When an observer wants to un-register,
        # we just take it off the list.
        try:
            self._observers.remove(observer)
        except ValueError:
            pass


class WeatherData(Subject):
    """monitor the object"""

    def __init__(self, name='', temperature=0, humidity=0, pressure=0):
        Subject.__init__(self)
        self.name = name
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure

    @property
    def temperature(self):
        return self._temperature

    @property
    def humidity(self):
        return self._humidity

    @property
    def pressure(self):
        return self._pressure

    @property
    def measurements(self):
        return (self._temperature, self._humidity, self._pressure)

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.notify()

    @humidity.setter
    def humidity(self, value):
        self._humidity = value
        self.notify()

    @pressure.setter
    def pressure(self, value):
        self._pressure = value
        self.notify()

    @measurements.setter
    def measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify()


class Observer:
    def __init__(self, name='', temperature=0, humidity=0, pressure=0):
        self.name = name
        self.temerature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def display(self):
        print("I am observing %s", self.name)

    def update(self):
        self.temerature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()


class CurrentConditionsDisplay(Observer):
    """Updates the CurrentConditionsDisplay viewer"""

    # The CurrentConditionsDisplay class should keep track of the temperature/humidity/pressure measurements and display them.
    def __init__(self, name='CurrentConditionsDisplay', temperature=0, humidity=0, pressure=0):
        Observer.__init__(self)

    def display(self, subject):
        print("Current Conditions For %s", subject.name)
        print("Temperature: %d F degrees", subject.temerature)
        print("Humidity: %d [%]", subject.humidity)
        print("Pressure: %d PSI", subject.pressure)


# TODO: Implement StatisticsDisplay Class
class StatisticsDisplay(Observer):
    """Updates the StatisticsDisplay viewer"""

    # The StatisticsDisplay class should keep track of the min/average/max measurements and display them.
    def __init__(self, name='StatisticsDisplay'):
        Observer.__init__(self)
        self._temerature_history = []
        self._humidity_history = []
        self._pressure_history = []
        # self.update()

    def update(self):
        self.temerature_min = min(self._temerature_history)
        self.temerature_max = max(self._temerature_history)
        self.temerature_average = sum(
            self._temerature_history)/len(self._temerature_history)

        self.humidity_min = min(self._humidity_history)
        self.humidity_max = max(self._humidity_history)
        self.humidity_average = sum(
            self._humidity_history)/len(self._humidity_history)

        self.pressure_min = min(self._pressure_history)
        self.pressure_max = max(self._pressure_history)
        self.pressure_average = sum(
            self._pressure_history)/len(self._pressure_history)
        self.display()

    def display(self):
        print("Current Statistics From %s", subject.name)
        print("         \t\t\t | min | avge | max |")
        print("Temperature:  \t| %d  |  %d  |  %d |",
              self.temerature_min, self.temerature_average, self.temerature_max)
        print("Humidity %:   \t| %d  |  %d  |  %d |",
              self.humidity_min, self.humidity_average, self.humidity_max)
        print("Pressure psi: \t| %d  |  %d  |  %d |",
              self.pressure_min, self.pressure_average, self.pressure_max)

# TODO: Implement ForecastDisplay Class.
class ForecastDisplay(Observer):
    """Updates the ForecastDisplay viewer"""

    # The ForecastDisplay class shows the weather forcast based on the current
    # temperature, humidity and pressure. Use the following formuals :
    # forcast_temp = temperature + 0.11 * humidity + 0.2 * pressure
    # forcast_humadity = humidity - 0.9 * humidity
    # forcast_pressure = pressure + 0.1 * temperature - 0.21 * pressure

    def update(self, subject):
        print('OctalViewer: Subject' + str(subject.name) +
              'has data '+str(oct(subject.data)))


"""main function"""
if __name__ == "__main__":
    """provide the data"""
    # TODO: Create two objects from StatisticsDisplay class and ForecastDisplay class.
    obj1 = WeatherData('Data 1')
    obj2 = WeatherData('Data 2')

    view1 = CurrentConditionsDisplay()
    view2 = StatisticsDisplay()
    view3 = ForecastDisplay()

    # TODO: Register them to the concerete instance of the Subject class so the they get the 'measurements' updates.
    obj1.attach(view1)
    obj1.attach(view2)
    obj1.attach(view3)
    obj1.measurements = 80, 65, 30.4
    # obj1.measurements = 80, 65, 30.4
    # un-register the observer
    obj1.removeObserver(current_display)
    obj1.measurements(120, 100, 1000)

    obj2.attach(view1)
    obj2.attach(view2)
    obj2.attach(view3)

    obj1.measurements(80, 65, 30.4)
    # obj1.measurements = 80, 65, 30.4
    # obj2.measurements = 80, 65, 30.4
