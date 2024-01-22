# Exercise: Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
# Import the math module to access mathematical functions like pi.
import math

# Create a base class Shape to represent a generic shape with methods for calculating area and perimeter.
class Shape:
    # Placeholder method for calculating area and calculating perimeter (will be implemented in derived classes).
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

# Create a derived class called Circle, which inherits from the Shape class.
class Circle(Shape):
     # Initialize the Circle object with a given radius
     def __init__(self, radius):
         self.radius = radius
     
    # Define a method to calculate and return the area of the circle.
     def calc_area(self):
         return round(self.radius**2 * math.pi, 2)
     
    # Define a method to calculate and return the perimeter of the circle.
     def calc_perimeter(self):
         return round(2 * math.pi * self.radius, 2)
     
# Create a derived class called Triangle, which inherits from the Shape class
class Triangle(Shape):
    # Initialize the Triangle object with a base, height, and three side lengths
    def __init__(self, base, height, side_a, side_b, side_c):
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    # Define a method to calculate and return the area of the triangle.
    def calc_area(self):
        return 0.5 * self.base * self.height
    
    # Define a method to calculate and return the perimeter of the triangle.
    def calc_perimeter(self):
        return self.side_a + self.side_b + self.side_c

# Create a derived class called Square, which inherits from the Shape class
class Square(Shape):
    # Initialize the Square object with given side length x.
    def __init__(self, x):
        self.x = x
        
    # Define a method to calculate and return the area of the square.
    def calc_area(self):
        return self.x * self.x
    
    # Define a method to calculate and return the perimeter of the square.
    def calc_perimeter(self):
        return 4 * self.x
    
# Create a derived class called Rectangle, which inherits from the Shape class.
class Rectangle(Shape):
    # Initialize the Rectangle object with given length and width.
    def __init__(self, l, w):
        self.l = l
        self.w = w

    # Define a method to calculate and return the area of the rectangle.
    def calc_area(self):
        return self.l * self.w
    
    # Define a method to calculate and return the perimeter of the rectangle.
    def calc_perimeter(self):
        return 2 * (self.l + self.w)

# Example usage: 
# Create the shape objects circle, triangle, square and rectangle, calculate their area and perimeter and print the results.
r = 20
circle = Circle(r)
circle_area = circle.calc_area()
circle_perimeter = circle.calc_perimeter()
print("\nThe circle area is: ", circle_area)
print("The circle perimeter is: ", circle_perimeter)

base = 7
height = 5
s1 = 5
s2 = 3
s3 = 4
triangle = Triangle(base, height, s1, s2, s3)
triangle_area = triangle.calc_area()
triangle_perimeter = triangle.calc_perimeter()
print("\nThe triangle area is: ", triangle_area)
print("The triangle perimeter is: ", triangle_perimeter)

s = 6
square = Square(s)
square_area = square.calc_area()
square_perimeter = square.calc_perimeter()
print("\nThe square area is: ", square_area)
print("The square perimeter is: ", square_perimeter)

length = 4
width = 5
rectangle = Rectangle(length, width)
rectangle_area = rectangle.calc_area()
rectangle_perimeter = rectangle.calc_perimeter()
print("\nThe rectangle area is: ", rectangle_area)
print("The rectangle perimeter is: ", rectangle_perimeter)

