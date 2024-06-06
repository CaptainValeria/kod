class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

# Kullanım
rect = Rectangle(4, 5)
print("Area:", rect.get_area())  # Area: 20
print("Perimeter:", rect.get_perimeter())  # Perimeter: 18
