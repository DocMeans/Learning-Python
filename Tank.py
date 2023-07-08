from math import pi as pi

class Tank:
  def __init__(self, height, radius): # Contructor that passes height and radius parameters
    self.height = height
    self.radius = radius 
  def  insideSurfaceArea(self): # Calculations 
    return (2 * pi * self.radius * self.height) + (2 * pi * self.radius**2)
  def  outsideSurfaceArea(self):
    return (2 * pi * self.radius * self.height)
  def  topOfTank(self): 
    return (pi * self.radius**2)
  def  volume(self): 
    return pi * self.radius**2 * self.height
  def  waterWeight(self): 
    return (pi * self.radius**2 * self.height) * 8
  def totalOutside(self):
    return (2 * pi * self.radius * self.height) + (pi * self.radius**2)
    
# Gather user input
print("To fing the out side, inside surface area and the volume and weight of the water")
height = float(input("How tall is the tank?: "))
radius = float(input("What is the radius of the tank?: "))

tank = Tank(height, radius) # Creates an object using the constructor and the parameters
print(f"The surface area inside the tank is: {round(tank.insideSurfaceArea(), 2)} sq feet") # results
print()
print(f"The surface area outside the tank is {round(tank.outsideSurfaceArea(), 2)} square feet")
print()
print(f"The area of the top of the tank is {round(tank.topOfTank(), 2)} square feet")
print()
print(f"The surface area outside for painting is {round(tank.totalOutside(), 2)} square feet")
print()
print(f"Volume of this tank is {round(tank.volume(), 2)} cubic feet")
print()
print(f"This tank holds {round(tank.volume(), 2)} gallons of water")
print()
print(f"The weight of the water is {round(tank.waterWeight(), 2)} lbs")
print()
# End of program