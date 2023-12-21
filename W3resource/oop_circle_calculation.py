# OOP - Exercise 1: 
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math

class Circle:
  def __init__(self, radius):
    self.radius = radius
    
    
  def calc_area(self):
    return self.radius**2 * math.pi   
    
    
  def calc_perimeter(self):
    return 2 * math.pi * self.radius
    
    
radius = float(input("Please enter a circle radius: "))

circle = Circle(radius)

area_result = circle.calc_area()
perimeter_result = circle.calc_perimeter()

print("The area result is: ", round(area_result, 2))
print("The perimeter result is: ", round(perimeter_result, 2))