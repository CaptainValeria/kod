from abc import ABC, abstractmethod

class Isci(ABC):
    @abstractmethod
    def is_yap(self):
        pass

class Muhendis(Isci):
    def is_yap(self):
        return "Mühendis çalışıyor"

class Teknisyen(Isci):
    def is_yap(self):
        return "Teknisyen çalışıyor"

# Kullanım
isciler = [Muhendis(), Teknisyen()]

for isci in isciler:
    print(isci.is_yap())




