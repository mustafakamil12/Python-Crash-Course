"""A set classes that can be used to represent electric cars."""

from car import Car

class ElectricCar(Car):
    """represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initilize attributes of the parent class."""

        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""

        print(f"This car has a {self.battery_size}-KWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""

        if self.battery.battery_size == 75:
            range = 260
        else:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self,battery_size=75):
        """Initilize the battery's attributes."""

        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""

        print(f"This car has a {self.battery_size}-KWh battery.")
