import argparse

def selamla(isim):
    print(f"Merhaba, {isim}!")

# Argümanları tanımlamak için ArgumentParser kullanılıyor
parser = argparse.ArgumentParser(description="Selamlama Programı")
parser.add_argument('isim', type=str, help="Selamlanacak kişinin ismi")

# Argümanlar ayrıştırılıyor
args = parser.parse_args()

# Selamla fonksiyonu çağrılıyor
selamla(args.isim)
