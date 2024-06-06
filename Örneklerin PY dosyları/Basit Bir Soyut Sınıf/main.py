from abc import ABC, abstractmethod 

class Hayvan(ABC): 
    @abstractmethod 
    def ses_cikar(self): 
        pass

class Kopek(Hayvan): 
    def ses_cikar(self): 
        return "Hav Hav"

class Kedi(Hayvan): 
    def ses_cikar(self): 
        return "Miyav"

kedi = Kedi() 
kopek = Kopek() 

print(kedi.ses_cikar())  # Miyav
print(kopek.ses_cikar()) # Hav Hav

