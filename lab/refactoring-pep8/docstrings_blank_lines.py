# by Kami Bigdely
# Docstrings and blank lines


class OnBoardTemperatureSensor:
    """
    This is a class for the onboard temperature sensor.

    Attributes: None
    """
    VOLTAGE_TO_TEMP_FACTOR = 5.6

    def __init__(self):
        """
        Constructor for OnboardTemperatureSensor.

        Parameters: None
        """
        pass

    def read_voltage(self):
        """
        Read voltage from onboard temperature sensor.

        Returns:
            float: The voltage.
        """
        return 2.7

    def get_temperature(self):
        """
        Calculate the temperature from voltage.

        Returns:
            int: The temperature in celcius.
        """
        return self.read_voltage() \
            * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR  # [celcius]


class CarbonMonoxideSensor:
    """
    This is a class for the carbon monoxide sensor.

    Attributes:
        on_board_temp_sensor (int): The onboard temperature.
        carbon_monoxide (float): The carbon monoxide level.
    """
    
    VOLTAGE_TO_CO_FACTOR = 0.048

    def __init__(self, temperature_sensor):
        """
        The constructor for the CarbonMonoxideSensor class.

        If argument "temperature_sensor" is not defined, then create a new
        OnBoardTemperatureSensor object.

        Args:
            temperature_sensor (float): The onboard temperature.
        """
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()

    def get_carbon_monoxide_level(self):
        """
        Get the carbon monoxide level and save it as an attribute.

        Returns:
            float: The carbon monoxide level.
        """
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = \
            CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(
                sensor_voltage, self.on_board_temp_sensor.get_temperature()
            )
        return self.carbon_monoxide

    def read_sensor_voltage(self):
        """
        Read the sensor voltage.

        In real life, it should read from hardware.

        Returns:
            float: The sensor voltage.
        """
        return 2.3

    def convert_voltage_to_carbon_monoxide_level(self, voltage, temperature):
        """
        Convert the voltage to carbon monoxide level.

        Args:
            voltage (float): The voltage.
            temperature (float): The temperature.

        Returns:
            float: The carbon monoxide level.
        """
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR \
            * temperature


class DisplayUnit:
    """
    This is a class to display messages.

    Attributes:
        string (str): Unknown.
    """
    def __init__(self):
        """The constructor for the DisplayUnit class."""
        self.string = ''

    def display(self, msg):
        """
        Print a message to the console.

        Args:
            msg (str): Message to be displayed.

        Returns: None
        """
        print(msg)


class CarbonMonoxideDevice():
    """
    This is a class for the carbon monoxide device.

    Attributes:
        co_sensor (CarbonMonoxideSensor): The carbon monoxide sensor.
        display_unit (DisplayUnit): The display unit.
    """
    def __init__(self, co_sensor, display_unit):
        """
        The constructor for the CarbonMonoxideDevice class.

        Args:
            co_sensor (CarbonMonoxideSensor): The carbon monoxide sensor.
            display_unit (DisplayUnit): The display unit.
        """
        self.carbonMonoxideSensor = co_sensor
        self.display_unit = display_unit

    def Display(self):
        """
        Create a message that displays the carbon monoxide level.

        Return: None
        """
        msg = 'Carbon Monoxide Level is : ' \
            + str(self.carbonMonoxideSensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)


if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.Display()
