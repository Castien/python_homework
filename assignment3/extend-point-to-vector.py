

# Task 5: Extending a Class
# Within the assignment3 folder, create a file called extend-point-to-vector.py.
# Create a class called Point. It represents a point in 2d space, with x and y values passed to the __init__() method. 
# It should include methods for equality, string representation, and Euclidian distance to another point.
# Create a class called Vector which is a subclass of Point and uses the same __init__() method. 
# Add a method in the vector class which overrides the string representation so Vectors print differently than Points. 
# Override the + operator so that it implements vector addition, summing the x and y values and returning a new Vector.
# Print results which demonstrate all of the classes and methods which have been implemented.


import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# method for equality:
# compares the two x and y point values, returns True if both match
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# method for string representation:
# how points appear when printed
    def __str__(self):
        return f"Point({self.x}, {self.y})"

# method for euclidian distance to another point:
# # d = sqrt of ((pointX1 - pointX2)^2 + (pointY1 - pointY2)^2)
# difference between the two points along the X-axis and Y-axis coordinates individually
# squared to get positive number
# square root using math.sqrt

# math.sqrt method
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Vector(Point):
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

# testing point
point1 = Point(2, 3)
point2 = Point(2, 3)
point3 = Point(5, 7)

print(point1)
print(point1 == point2)
print(point1.distance(point3))

# testing vector
vector1 = Vector(2, 3)
vector2 = Vector(4, 5)

print(vector1)
print(vector1 == vector2)
print(vector1.distance(vector2))
print(vector1 + vector2)


