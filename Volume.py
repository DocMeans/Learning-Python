# Written by: Franklin Means on 6/11/2023
# This program allows you to calculate the volume of an object
# by entering the length, width, and height of the object.

# Ask the user for the length, width, and height of the object. And convert the string to a float.
length = float(input("Enter the length of the object: "))
width = float(input("Enter the width of the object: "))
height = float(input("Enter the height of the object: "))

# Calculate the volume of the object.
volume = length * width * height

# Display the volume of the object.
print("The volume of the object is: ", volume)