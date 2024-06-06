class Hayvan:
    def __init__(self, isim):
        self.isim = isim

    def ses_cikar(self):
        pass  # Bu metod soyutlanmıştır, alt sınıflar tarafından implement edilmelidir.

class Kedi(Hayvan):
    def ses_cikar(self):
        return "Miyav"

# Kullanım
kedi = Kedi("Minnak")
print(f"{kedi.isim}: {kedi.ses_cikar()}")



