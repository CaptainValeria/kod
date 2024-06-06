class Ucak:
    def uc(self):
        return "Uçak uçuyor"

class Helikopter:
    def uc(self):
        return "Helikopter uçuyor"

class Kus:
    def uc(self):
        return "Kuş uçuyor"

def uc_eylemi(arac):
    print(arac.uc())

# Kullanım
ucak = Ucak()
helikopter = Helikopter()
kus = Kus()

uc_eylemi(ucak)  # Uçak uçuyor
uc_eylemi(helikopter)  # Helikopter uçuyor
uc_eylemi(kus)  # Kuş uçuyor



