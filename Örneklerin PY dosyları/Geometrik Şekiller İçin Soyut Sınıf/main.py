from abc import ABC, abstractmethod 

class Sekil(ABC):
    @abstractmethod 
    def alan(self):
        pass 

class Kare(Sekil):
    def __init__(self, kenar):
        self.kenar = kenar 
    def alan(self):
        return self.kenar ** 2 

class Daire(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap 
    def alan(self):
        return 3.14 * (self.yaricap ** 2) 

kare = Kare(5)
daire = Daire(3)

print(f"Kare alanı: {kare.alan()}")
print(f"Daire alanı: {daire.alan()}")


