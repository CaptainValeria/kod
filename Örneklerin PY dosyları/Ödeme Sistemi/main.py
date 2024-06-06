from abc import ABC, abstractmethod

class Odeme(ABC):
    @abstractmethod
    def odeme_yap(self, miktar):
        pass

class KrediKartiOdeme(Odeme):
    def odeme_yap(self, miktar):
        return f"Kredi kartı ile {miktar} TL ödendi."

class PayPalOdeme(Odeme):
    def odeme_yap(self, miktar):
        return f"PayPal ile {miktar} TL ödendi."

# Kullanım
kredi_karti = KrediKartiOdeme()
paypal = PayPalOdeme()

print(kredi_karti.odeme_yap(100))  # Kredi kartı ile 100 TL ödendi.
print(paypal.odeme_yap(200))       # PayPal ile 200 TL ödendi.





