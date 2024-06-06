from abc import ABC, abstractmethod

class Hayvan(ABC):
    @abstractmethod
    def ses_cikar(self):
        pass

class Kopek(Hayvan):
    def ses_cikar(self):
        return "Hav hav"

class Kedi(Hayvan):
    def ses_cikar(self):
        return "Miyav"

# Kullanım
kopek = Kopek()
kedi = Kedi()

print(kopek.ses_cikar())  # Hav hav
print(kedi.ses_cikar())   # Miyav



