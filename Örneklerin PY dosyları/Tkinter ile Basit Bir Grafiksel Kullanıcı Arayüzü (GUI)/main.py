import tkinter as tk
from tkinter import messagebox

# Pencereyi oluştur
root = tk.Tk()
root.title("Basit GUI Örneği")

# Pencere boyutunu sabitle
root.geometry("300x150")
root.resizable(False, False)

# Etiket ve giriş alanı (İsim)
label_isim = tk.Label(root, text="İsim:")
label_isim.grid(row=0, column=0, padx=10, pady=10)

entry_isim = tk.Entry(root)
entry_isim.grid(row=0, column=1, padx=10, pady=10)

# Etiket ve giriş alanı (Yaş)
label_yas = tk.Label(root, text="Yaş:")
label_yas.grid(row=1, column=0, padx=10, pady=10)

entry_yas = tk.Entry(root)
entry_yas.grid(row=1, column=1, padx=10, pady=10)

# Butona tıklanınca çalışacak fonksiyon
def bilgileri_goster():
    isim = entry_isim.get()
    yas = entry_yas.get()
    if isim and yas:
        try:
            yas = int(yas)
            messagebox.showinfo("Bilgiler", f"İsim: {isim}\nYaş: {yas}")
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli bir yaş giriniz.")
    else:
        messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldurunuz.")

# Gönder butonu
button_gonder = tk.Button(root, text="Gönder", command=bilgileri_goster)
button_gonder.grid(row=2, column=0, columnspan=2, pady=10)

# Pencereyi çalıştır
root.mainloop()