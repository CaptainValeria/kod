from abc import ABC, abstractmethod

class Tasit(ABC):
    @abstractmethod
    def hareket_et(self):
        pass

class Araba(Tasit):
    def hareket_et(self):
        return "Araba yolda gidiyor."

class Bisiklet(Tasit):
    def hareket_et(self):
        return "Bisiklet yolda gidiyor."

# Kullanım
araba = Araba()
bisiklet = Bisiklet()

print(araba.hareket_et())
print(bisiklet.hareket_et())


