class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Kullanım
dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Kitty says Meow!


