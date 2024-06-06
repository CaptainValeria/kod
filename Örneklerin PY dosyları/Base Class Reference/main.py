class Sekil:
    def alan(self):
        pass

class Kare(Sekil):
    def __init__(self, kenar):
        self.kenar = kenar

    def alan(self):
        return self.kenar * self.kenar

class Daire(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap

    def alan(self):
        return 3.14 * self.yaricap * self.yaricap

# Kullanım
sekiller = [Kare(4), Daire(3)]

for sekil in sekiller:
    print(f"Alan: {sekil.alan()}")


