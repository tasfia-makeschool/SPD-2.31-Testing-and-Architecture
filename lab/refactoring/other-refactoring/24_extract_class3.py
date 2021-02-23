# by Kami Bigdely
# Extract class
WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05

class Steak:
    def __init__(self, time, temp, pressure, desired_state):
        self.time = time
        self.temperature = temp
        self.pressure = pressure
        self.desired_state = desired_state

    def is_cookeding_criteria_satisfied(self):
        if self.is_well_done() or self.is_medium():
            print('cooking is done.')
        else:
            print('ongoing cooking')
    
    def is_well_done(self):
        return self.desired_state == 'well-done' and  \
            self.get_cooking_progress() >= WELL_DONE
    
    def is_medium(self):
        return self.desired_state == 'medium' and  \
            self.get_cooking_progress() >= MEDIUM

    def get_cooking_progress(self):
        return self.time * self.temperature * self.pressure * COOKED_CONSTANT


# def is_cookeding_criteria_satisfied(time, temperature, 
#                                     pressure, desired_state):
#     return is_well_done(time, temperature, pressure, desired_state) or \
#            is_medium(time, temperature, pressure, desired_state)


# def is_well_done(time, temperature, pressure, desired_state):    
#     return desired_state == 'well-done' and  \
#            get_cooking_progress(time, temperature, pressure) >= WELL_DONE


# def is_medium(time, temperature, pressure, desired_state):
#     return desired_state == 'medium' and  \
#            get_cooking_progress(time, temperature, pressure) >= MEDIUM

# def get_cooking_progress(time, temperature, pressure):
#     return time * temperature * pressure * COOKED_CONSTANT


time = 30 # [min]
temp = 103 # [celcius]
pressure = 20 # [psi]
desired_state = 'well-done'

steak = Steak(time, temp, pressure, desired_state)
steak.is_cookeding_criteria_satisfied()

# if is_cookeding_criteria_satisfied(time, temp, pressure, desired_state):
#     print('cooking is done.')
# else:
#     print('ongoing cooking.')
