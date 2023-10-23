import tkinter as tk

form = tk.Tk()
form.title("Basit Giriş Uygulaması")
windowX = (form.winfo_screenwidth() // 2) - 250
windowY = (form.winfo_screenheight() // 2) - 250
form.geometry("500x500+{}+{}".format(windowX, windowY))
form.minsize(500, 500)

# DEMO HESAP
kAdi = "kursat"
kSifre = "123456"

kullaniciAdi = tk.Entry()
kullaniciAdi.insert(0, "Kullanıcı Adınız")
kullaniciSifre = tk.Entry()
kullaniciSifre.insert(0, "Şifreniz")
label = tk.Label(text="Kullanıcı adı ve Şifrenizi giriniz!")
uyari = tk.Label(text="Giriş hakkınız bitmiştir.", fg="red")
denemeHakki = 3


def giris():
    def ekranitemizle():
        for a in form.winfo_children():
            a.destroy()
    global denemeHakki

    if kullaniciAdi.get() == kAdi and kullaniciSifre.get() == kSifre:
        ekranitemizle()
        label2 = tk.Label(text="Hoşgeldiniz {}".format(kAdi))
        label2.pack()
    else:
        label.config(text="Bilgiler yanlış! {} deneme hakkınız kaldı.".format(denemeHakki), fg="orange")
        denemeHakki -= 1
        if denemeHakki < 0:
            label.config(text="Giriş hakkınız bitmiştir.", fg="red")
            btn.config(state="disabled")


btn = tk.Button(form, text="Giriş Yap", command=giris)
kullaniciAdi.pack()
kullaniciSifre.pack()
label.pack()
btn.pack()

form.mainloop()
