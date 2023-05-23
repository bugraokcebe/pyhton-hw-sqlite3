import sqlite3


def signUp():
    db = sqlite3.connect('C:/Users/asus/Desktop/odev/banka.db')
    imlec = db.cursor()
     
    tcIn = int(input())
    parolaIn = input()
    bakiyeIn = int(input())

    imlec.execute("INSERT INTO musteri VALUES (?,?,?)",(tcIn,parolaIn,bakiyeIn))

    db.commit()
    db.close()

def signIn():
    db = sqlite3.connect('C:/Users/asus/Desktop/odev/banka.db')
    imlec = db.cursor()
    global tcIn
    print("Tc kimlik numaranızı giriniz")
    tcIn = int(input())
    print("Parolanızı giriniz")
    parolaIn = input()

    imlec.execute('SELECT * FROM musteri')
    girisDegeri = 0

    for veriler in imlec:
        if tcIn == veriler[0] and parolaIn == veriler[1]:
            girisDegeri = 1
        
    
    if girisDegeri == 1:
        print("Giriş yapıldı -- Uygulama ekranına yönlendiriliyorsunuz")
        appMenu()
    else:
        print("Giriş Yapılamadı - Tc kimlik numaranız veya şifreniz hatalı!")
                  
    db.commit()
    db.close()

def appMenu():
    print("MENÜ")
    print("Yapmak istediğiniz işlemi seçiniz.")
    print("1-> Göster")
    print("2-> Nakit Ekle")
    print("3-> Nakit Çek")
    print("4-> Nakit Gönder")
    print("5-> Çıkış")

    secim=int(input())

    if secim==1:
        db = sqlite3.connect('C:/Users/asus/Desktop/odev/banka.db')
        imlec = db.cursor()

        komut = """SELECT * FROM musteri WHERE musteriTC = {}""".format(tcIn)

        imlec.execute(komut)

        for veri in imlec:
            print("TL " ,veri[2])
        
        db.commit()
        appMenu()

    elif secim==2:
        db = sqlite3.connect('C:/Users/asus/Desktop/odev/banka.db')
        imlec = db.cursor()
        print("Eklenecek Tutarı Giriniz: ")
        eklenecekTutar = int(input())

        komut = "UPDATE musteri SET musBakiye = musBakiye + ? WHERE musteriTC = ?"

        imlec.execute(komut,(eklenecekTutar,tcIn))

        print(eklenecekTutar , "TL eklendi...")

        for veri in imlec:
            print("TL " ,veri[2])
        db.commit()
        appMenu()
    elif secim==3:
        db = sqlite3.connect('C:/Users/asus/Desktop/odev/banka.db')
        imlec = db.cursor()
        print("Çekilecek Tutarı Giriniz: ")
        cekilenTutar = int(input())

        komut = "UPDATE musteri SET musBakiye = musBakiye - ? WHERE musteriTC = ?"

        imlec.execute(komut,(cekilenTutar,tcIn))

        print(cekilenTutar , "TL çekildi...")
        db.commit()
        appMenu()
    elif secim==4:
        db = sqlite3.connect('C:/Users/asus/Desktop/odev/banka.db')
        imlec = db.cursor()
        print("TL göndereceğiniz kişinin TC kimlik numarasını giriniz:")
        transferTcNo = int(input())
        print("Miktarı giriniz:")
        transferTL = int(input())

        komut = "UPDATE musteri SET musBakiye = musBakiye - ? WHERE musteriTC = ?"

        imlec.execute(komut,(transferTL,tcIn))

        print("Hesabınızdan ", transferTL , " TL gönderildi...")

        komut = "UPDATE musteri SET musBakiye = musBakiye + ? WHERE musteriTC = ?"

        imlec.execute(komut,(transferTL,transferTcNo))

        print("İşlem Başarıyla Tamamlandı...")

        db.commit()

        appMenu()
    else:
        print("çıkışş")


 
    
while True:
    print("ANA MENÜ")
    print("Yapmak istediğiniz işlemi seçiniz.")
    print("1-> Giriş")
    print("2-> Kayıt Ol")
    secim=int(input())

    if secim==1:
        signIn()
    elif secim==2:
        signUp()
    else:
        exit