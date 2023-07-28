from math import pi as pie

class Tank:
    '''This class correctly computes different params'''
    def __init__(self, height, radius): # Contructor that passes height and radius parameters
        self.height = height
        self.radius = radius
    def inside_surface_area(self):
        '''Calculation for the inside surface area'''
        return 2 * pie * self.radius * self.height + 2 * pie * self.radius**2
    def  outside_surface_area(self):
        '''Calculation for the outside surface area'''
        return 2 * pie * self.radius * self.height
    def  top_of_tank(self):
        '''Calculation for the top of the tank'''
        return pie * self.radius**2
    def  volume(self):
        '''Calculation for the volume'''
        return pie * self.radius**2 * self.height
    def  gallons(self):
        '''Calculation for the volume'''
        volume = pie * self.radius**2 * self.height
        gallons = volume * 7.47
        return gallons
    def  water_weight(self):
        '''Returns a float value for the weight of the water in the tank'''
        volume = pie * self.radius**2 * self.height
        gallons = volume * 7.47
        weight = gallons * 8.33
        return weight
    def total_outside(self):
        '''Returns a value for the total outside paintable surface'''
        return 2 * pie * self.radius * self.height + pie * self.radius**2

print("To fing the out side, inside surface area and the volume and weight of the water")
# Gather user input for calculating the various aspects of the tank
how_round = float(input("Measured in feet, what is the radius of the tank?: "))
how_tall = float(input("Measured in feet, how tall is the tank?: "))

'''Creates an object using the constructor and the parameters'''
tank = Tank(how_tall, how_round)
print(f"The surface area inside the tank is: {round(tank.inside_surface_area(), 2)} sq feet")
print(f"The surface area outside the tank is {round(tank.outside_surface_area(), 2)} square feet")
print(f"The area of the top of the tank is {round(tank.top_of_tank(), 2)} square feet")
print(f"The surface area outside for painting is {round(tank.total_outside(), 2)} square feet")
print(f"Volume of this tank is {round(tank.volume(), 2)} cubic feet")
print(f"This tank holds {round(tank.gallons(), 2)} gallons of water")
print(f"The weight of the water is {round(tank.water_weight(), 2)} lbs")
# End of program