# Resources
# https://www.geeksforgeeks.org/observer-method-python-design-patterns/
# https://docs.google.com/document/d/1jyrxxQyrVxBG9S_hXYI69ytUMdxQdApyM6MO2CwvYj4/edit


class Subject:
    """Represents what is being observed"""

    def __init__(self):
        """create an empty observer list"""
        self._observers = []

    def notify(self, measurements=None):
        """Alert the observers"""
        # We notify the observers when we get updated measurements from the Weather Station.
        for observer in self._observers:
            if measurements != observer:
                observer.update(measurements)

    # Both of the following two methods take an observer as an argument;
    # That is, the observer to be registered or removed.
    # In our case CurrentConditionsDisplay, StatisticsDisplay & ForecastDisplay.
    def attach(self, observer):
        """If the observer is not in the list, append it into the list"""
        # When an observer registers, we just add it to the end of the list. 
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """Remove the observer from the observer list"""
        # When an observer wants to un-register, we just take it off the list.
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

class WeatherData(Subject):
    """Class/Object to be monitored and observed"""

    def __init__(self, name='WeatherData', temperature=0, humidity=0, pressure=0):
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

    def setMeasurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify()


class Observer:
    def __init__(self, name='Default-Observer-Interface'):
        self.name = name

    def update(self, measurements):
        print("Updated: \n", self.display(), "with: ", measurements)

    def display(self):
        print("Observer: ", self.name)



class CurrentConditionsDisplay(Observer):
    """Updates the CurrentConditionsDisplay viewer"""

    # The CurrentConditionsDisplay class should keep track of the temperature/humidity/pressure measurements and display them.
    def __init__(self, name='CurrentConditionsDisplay', subject=None):
        Observer.__init__(self, name)
        self._subject = subject

    def update(self, measurements):
        self.display()
    #     self._temperature = measurements[0]
    #     self._humidity = measurements[1]
    #     self._pressure = measurements[2]
    #     self.notify()

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

    def update(self):
        print('OctalViewer: Subject' + str(subject.name) +
              'has data '+str(oct(subject.data)))


"""main function"""
if __name__ == "__main__":
    """provide the data"""
    WeatherStation = WeatherData('Data 1')
    print(WeatherStation.measurements)

    view1 = CurrentConditionsDisplay()
    WeatherStation.attach(view1)
    print(WeatherStation.measurements)

    WeatherStation.setMeasurements(30, 85, 60.8)
    print(WeatherStation.measurements)

    # TODO: Create Two Objects A StatisticsDisplay Class & A ForecastDisplay Class.
    # view2 = StatisticsDisplay()
    # view3 = ForecastDisplay()

    # TODO: Register them to the concerete instance of the Subject class so the they get the 'measurements' updates.
    # WeatherStation.attach(view2)
    # WeatherStation.attach(view3)

    # TODO: Test our Statistics & Forecast Display by Adding/Setting the Messurement Vaules
    # WeatherStation.setMeasurements(80, 65, 30.4)
    # print(WeatherStation.measurements)

    # TODO: Un-Register the CurrentConditionsDisplay observer & Test our subscription tracking
    # WeatherStation.removeObserver(view1)
    # WeatherStation.setMeasurements(120, 100, 1000)

    # WeatherStation.measurements = 80, 65, 30.4
