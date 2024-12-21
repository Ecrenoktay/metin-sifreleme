import random

def sezar_sifrele_turkce(metin, anahtar):
    turkce_karakterler = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZabcçdefgğhıijklmnoöprsştuüvyz"
    sifreli_metin = ""
    
    for harf in metin:
        if harf in turkce_karakterler:
            index = turkce_karakterler.index(harf)
            yeni_index = (index + anahtar) % len(turkce_karakterler)
            sifreli_metin += turkce_karakterler[yeni_index]
        else:
            sifreli_metin += harf  # Türkçe olmayan karakterleri aynen ekle
    return sifreli_metin

def sezar_coz_turkce(sifreli_metin, anahtar):
    return sezar_sifrele_turkce(sifreli_metin, -anahtar)


def sezar_sifrele(metin, anahtar):
    sifreli_metin = ""
    for harf in metin:
        if harf.isalpha():
            ascii_baslangic = 65 if harf.isupper() else 97
            sifreli_harf = chr((ord(harf) - ascii_baslangic + anahtar) % 26 + ascii_baslangic)
            sifreli_metin += sifreli_harf
        else:
            sifreli_metin += harf
    return sifreli_metin


def sezar_coz(sifreli_metin, anahtar):
    return sezar_sifrele(sifreli_metin, -anahtar)


def vigenere_sifrele(metin, anahtar):
    sifreli_metin = ""
    anahtar = [ord(h) - 65 if h.isupper() else ord(h) - 97 for h in anahtar]
    anahtar_uzunluk = len(anahtar)

    for i, harf in enumerate(metin):
        if harf.isalpha():
            ascii_baslangic = 65 if harf.isupper() else 97
            kaydirma = anahtar[i % anahtar_uzunluk]
            sifreli_harf = chr((ord(harf) - ascii_baslangic + kaydirma) % 26 + ascii_baslangic)
            sifreli_metin += sifreli_harf
        else:
            sifreli_metin += harf
    return sifreli_metin


def vigenere_coz(sifreli_metin, anahtar):
    cozum_anahtari = "".join(
        chr(65 + (26 - (ord(h) - 65 if h.isupper() else ord(h) - 97)) % 26) for h in anahtar
    )
    return vigenere_sifrele(sifreli_metin, cozum_anahtari)


def main():
    print("Metin Şifreleme ve Çözme Programına Hoş Geldiniz!")
    print("1. Sezar Şifreleme")
    print("2. Vigenère Şifreleme")
    secim = input("Bir şifreleme yöntemi seçin (1 veya 2): ")

    if secim not in {"1", "2"}:
        print("Geçersiz seçim!")
        return
    
    turkce_desteği = (secim == "1") and input("Türkçe karakter desteği kullanılsın mı? (Evet/Hayır): ").strip().lower() == "evet"

    metin =  input("Şifrelenecek metni girin: ")

    rastgele_anahtar = input("Anahtarı rastgele oluşturulsun mu? (Evet/Hayır): ").lower()
    if rastgele_anahtar == "evet":
        anahtar = random.randint(1, 25) if secim == "1" else ''.join(
            random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
        print(f"Rastgele oluşturulan anahtar: {anahtar}")
    else:
        anahtar = int(input("Kaydırma anahtarını girin (ör. 3): ")) if secim == "1" else input("Anahtar kelimeyi girin: ")
    
    if secim == "1":
        if turkce_desteği:
            sifreli_metin = sezar_sifrele_turkce(metin, anahtar)
            cozulmus_metin = sezar_coz_turkce(sifreli_metin, anahtar)
        else:
            sifreli_metin = sezar_sifrele(metin, anahtar)
            cozulmus_metin = sezar_coz(sifreli_metin, anahtar)
    else:
        sifreli_metin = vigenere_sifrele(metin, anahtar)
        cozulmus_metin = vigenere_coz(sifreli_metin, anahtar)
        
    print(f"Şifrelenmiş metin: {sifreli_metin}")
    print(f"Çözülmüş metin: {cozulmus_metin}")

if __name__ == "__main__":
    main()
