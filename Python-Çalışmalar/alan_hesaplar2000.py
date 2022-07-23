def ucgen_alan(taban, yukseklik):
    alan = float(taban)*float(yukseklik)/2
    print("Ucgenin alani = {0}".format(alan))


def dikdortgen_alan(kisa_kenar, uzun_kenar):
    alan = float(kisa_kenar)*float(uzun_kenar)
    print("Dikdortgenin alani = {0}".format(alan))


def daire_alan(yaricap):
    pi = 3.14
    alan = pi*(float(yaricap)*float(yaricap))
    print("Dairenin alani = {0}".format(alan))


def kare_alan(kenar):
    alan = float(kenar)*float(kenar)
    print("Karenin alani = {0}".format(alan))

    
print("1- Üçgenin Alanı >")
print("2- Dİkdörtgenin Alanı >")
print("3- Dairenin Alanı >")
print("4- Karenin Alanı >")
devam = True
while devam:

    islem = int(input("Lütfen işlem Giriniz : "))

    if islem == (1):
        taban = input("Lütfen taban uzunlugunu giriniz : ")
        yukseklik = input("Lütfen yükseklik giriniz : ")
        ucgen_alan(taban, yukseklik)
    elif islem == (2):
        a = input("Lütfen kısa kenar uzunluğunu giriniz : ")
        b = input("Lütfen uzun kenar uzunluğunu giriniz : ")
        dikdortgen_alan(a, b)
    elif islem == (3):
        r = input("Lütfen yarıçap uzunluğunu giriniz : ")
        daire_alan(r)
    elif islem == (4):
        a = input("Lütfen kenar uzunluğunu giriniz : ")
        kare_alan(a)
    else:
        print("İşleminiz Bitmiştir... İyi günler :)")
        devam = False
