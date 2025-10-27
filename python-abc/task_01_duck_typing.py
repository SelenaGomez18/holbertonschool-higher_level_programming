#!/usr/bin/python3
"""Module defining abstract Shape class, Circle and Rectangle, and a shape_info function."""


from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

class Circle(Shape):
    """Circle shape class."""

    def __init__(self, radius):
        """Initialize circle with a radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Rectangle shape class."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
def shape_info(shape):
    """Print the area and perimeter of any shape using duck typing."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
        