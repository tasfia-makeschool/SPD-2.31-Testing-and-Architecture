# Kami Bigdely
# Move Field

class Car:
    def __init__(self, engine, wheels, cabin, fuel_tank):
        self.engine = engine
        self.wheels = wheels
        self.cabin = cabin
        self.fuel_tank = fuel_tank
        # Set wheels' car reference into each wheel.
        for w in wheels:
            w.set_car(self)


class Wheel:
    def __init__(self, tpms_di, car=None, wheel_location=None):
        self.tpms_list = tpms_di  # Tire Pressure Monitoring System.
        self.car = car
        self.wheel_location = wheel_location

    def install_tire(self):
        print('remove old tube.')
        print('cleaned tpms: ', 
              self.tpms_di[self.wheel_location].get_serial_number, '.')
        print('installed new tube.')        
        
    def read_tire_pressure(self):
        return self.tpms_di[self.wheel_location].get_pressure()
    
    def set_car(self, car):
        self.car = car


class Tpms:
    """Tire Pressure Monitoring System."""
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.sensor_transmit_range = 300 # [feet]
        self.sensor_pressure_range = (8,300) # [PSI]
        self.battery_life = 6 # [year]
        
    def get_pressure(self):
        return 3
    
    def get_serial_number(self):
        return self.serial_number


class Engine:
    def __init__(self):
        pass


class FuelTank:
    def __init__(self):
        pass


class Cabin:
    def __init__(self):
        pass    
    

engine = Engine()

wheels = [
    Wheel(Tpms(983408543), None, 'front-right'),
    Wheel(Tpms(4343083), None, 'front-left'),
    Wheel(Tpms(23654835), None, 'back-right'),
    Wheel(Tpms(3498857), None, 'back-left')
]

cabin  = Cabin()

fuel_tank = FuelTank()

my_car = Car(engine, wheels, cabin, fuel_tank)


