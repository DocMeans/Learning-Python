from math import pi as pie

gallon_per_sqft = 7.47
gallon_weight = 8.33

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
        return tank.volume() * gallon_per_sqft
    def  water_weight(self):
        '''Returns a float value for the weight of the water in the tank'''
        return tank.gallons() * gallon_weight
    def total_outside(self):
        '''Returns a value for the total outside paintable surface'''
        return 2 * pie * self.radius * self.height + pie * self.radius**2

print("To fing the out side, inside surface area and the volume and weight of the water")
# Gather user input for calculating the various aspects of the tank
how_round = float(input("Measured in feet, what is the radius of the tank?: "))
how_tall = float(input("Measured in feet, how tall is the tank?: "))

'''Creates an object using the constructor and the parameters'''
tank = Tank(how_tall, how_round)
print(f"Surface area inside: {round(tank.inside_surface_area(), 2)} sq feet")
print(f"The outside surface area: {round(tank.outside_surface_area(), 2)} square feet")
print(f"Top of the tank is: {round(tank.top_of_tank(), 2)} square feet")
print(f"The paintable surface area outside: {round(tank.total_outside(), 2)} square feet")
print(f"Volume of this tank is: {round(tank.volume(), 2)} cubic feet")
print(f"This tank holds: {round(tank.gallons(), 2)} gallons of water at {round(tank.water_weight(), 2)} lbs")

# End of program