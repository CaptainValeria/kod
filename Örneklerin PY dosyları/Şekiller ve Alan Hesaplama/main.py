from abc import ABC, abstractmethod

class Sekil(ABC):
    @abstractmethod
    def alan(self):
        pass

class Daire(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap
    def alan(self):
        return 3.14 * self.yaricap * self.yaricap

class Dikdortgen(Sekil):
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik
    def alan(self):
        return self.genislik * self.yukseklik

# Kullanım
daire = Daire(5)
dikdortgen = Dikdortgen(4, 6)

print(daire.alan())        # 78.5
print(dikdortgen.alan())   # 24




