def hesapla_faiz(anapara, oran, yil):
    return anapara * (1 + oran)**yil

faiz = hesapla_faiz(1000, 0.05, 5)
print(f"Faizli Tutar: {faiz:.2f}")





