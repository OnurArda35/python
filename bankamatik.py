hesaplar = {

    "hesapA" : {
        "ad" : "Onur Arda",
        "hesapNo" : "1234567890",
        "sifre" : "179164Oa",
        "bakiye" : 3000,
        "ekHesap" : 2000
    },

    "hesapB" : {
        "ad" : "Rabia Top",
        "hesapNo" : "1234567891",
        "sifre" : "454545Rt",
        "bakiye" : 2000,
        "ekHesap" : 1000
    },

    "hesapC" : {
        "ad" : "İsa Demir",
        "hesapNo" : "1234567892",
        "sifre" : "qwerty",
        "bakiye" : 5500,
        "ekHesap" : 1000
    },

    "hesapD" : {
        "ad" : "Okan Ayaz",
        "hesapNo" : "1234567893",
        "sifre" : "18811938",
        "bakiye" : 4500,
        "ekHesap" : 1000
    }
}



def paraCek(hesap , miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap["bakiye"] >= miktar:
        hesap['bakiye'] -= miktar
        print(f"Paranizi alabilirsiniz. \nKalan Bakiye: {hesap['bakiye']} \nEk Hesap Bakiye: {hesap['ekHesap']} ")

    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if toplam >= miktar:
            ekHesapKullanimi = input("Ek Hesap Kullanılsın mı? 'E' yada 'H' ").upper()

            if ekHesapKullanimi == 'E':
                ekHesapEksi = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapEksi
                print(f"Paranizi alabilirsiniz. \nKalan Bakiye: {hesap['bakiye']} \nEk Hesap Bakiye: {hesap['ekHesap']} ")

            
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızın bilgileri şöyledir. \nBakiye: {hesap['bakiye']} \nEk Hesap Bakiye: {hesap['ekHesap']}")

        else:
            print(f"Üzgünüz. Bakiyeniz yetersiz. \nBakiye: {hesap['bakiye']} \nEk Hesap Bakiye: {hesap['ekHesap']}")




def paraYatir(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")    
    if input("Ana hesaba mı ('A'), Ek hesaba mı('E')?: ").upper() == 'A':
        hesap['bakiye']+= miktar
        print(f"Yeni ana hesap bakiyeniz: {hesap['bakiye']}")

    else:
        hesap['ekHesap']+= miktar
        print(f"Yeni ek hesap bakiyeniz: {hesap['ekHesap']}")



def bakiyeSorgu(hesap):
    print(f"Merhaba {hesap['ad']}")
    print(f"Ana hesap bakiyeniz: {hesap['bakiye']} \nEk hesap bakiyeniz: {hesap['ekHesap']}")



def paraYolla(hesap):
    gonHesapNo = input("Para gönderilecek hesap numarasını yazınız: ")
    miktar = int(input("Gonderilecek miktarı yazınız: "))

    
    if hesap['bakiye'] >= miktar:
        for key,value in hesaplar.items() :
            if gonHesapNo == (hesaplar[key]['hesapNo']):
                hesaplar[str(key)]['bakiye'] += miktar
                hesap['bakiye'] -= miktar
                print(f"Hesabınızdan {gonHesapNo} numaralı hesaba {miktar} bakiye gönderilmiştir. \nYeni bakiyeniz: {hesap['bakiye']} ")

    else:
        print("Hesabınızda yeterli miktar bulunmuyor.")

