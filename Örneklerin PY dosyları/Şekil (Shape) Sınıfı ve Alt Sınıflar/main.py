class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Kullanım
circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 4, 6)

print(f"Circle area: {circle.area()}")  # Circle area: 78.5
print(f"Rectangle area: {rectangle.area()}")  # Rectangle area: 24


