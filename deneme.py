#adminlerin kullanıcı adları ve şifreleri
adminler= {"admin1":{"kullanici_adi":"admin1", "sifre":"sifre123"},
           "admin2":{"kullanici_adi":"admin2", "sifre":"sifre321"}}


# Admin giriş ekranı
def admin_girisi():
    print("Lütfen admin girişi için admin kullanıcı adınızı ve şifrenizi giriniz.")
    admin_adi = input("Admin Kullanıcı Adı: ")
    admin_sifresi = input("Admin Şifre: ")

    if admin_adi in adminler:
        if admin_sifresi==adminler[admin_adi]["sifre"]:
            print("Admin girişi başarıyla yapılmıştır.")
        else:
            print("Hatalı şifre!")
    else:
        print("Hatalı kullanıcı adı!")
  
    
# Kullanıcı giriş ekranı
def kullanici_girisi():
    menu=["1-Sisteme üye ol","2-Sisteme giriş yap","3-Şifremi unuttum"]
   
    print(menu)
    secim=int(input(print("Lütfen yapmak istediğiniz seçeneği giriniz:")))
        
        
    #üye olma menüsü(ad-soay, tel no, tc no, adres , şifre girişi yapılır)
    if secim==1:
        print("-SİSTEME ÜYE OL-")
        ad_soyad=input(print("Adınızı ve soyadınızı giriniz:"))
        kullanici_adi=input(print("Kullanıcı adı giriniz:"))
        while True: #tel no da sadece rakam girişi yapma
            tel_no=input(print("Telefon numaranızı giriniz:"))
            if tel_no.isdecimal():
                break
            else:
                print("Hatıl giriş yaptınız. Lütfen sadece rakam giriniz.")
                    
        e_posta=input(print("Lütfen e-posta adresinizi giriniz:"))
            
        while True: #tc no da sadece rakam girişi yapma
            tc_no=input(print("TC numaranızı giriniz:"))
            if tc_no.isdecimal():
                break
            else:
                print("Hatıl giriş yaptınız. Lütfen sadece rakam giriniz.")
                    
        adres=input(print("Lütfen adresinizi giriniz:"))
        sifre=input(print("Lütfen bir şifre giriniz:"))
        print("\nSİSTEME ÜYE OLUNDU!!! \n\n")
           
            
    #tel no ya da eposta adresi ile sisteme giriş yapma
    elif secim==2:
        print("-SİSTEME GİRİŞ YAP-")
        giris_secim=input(print("""Sisteme telefon numarası ile giriş yapmak için '7'ye, 
                                e-posta adresi ile giriş yapmak için '8'ye basınız:"""))
        #tel no ile giriş yapma
        if giris_secim=="7":
            while True: #tel no da sadece rakam girişi yapma
                tel_no=input(print("Telefon numaranızı giriniz:"))
                if tel_no.isdecimal():
                    break 
                else:
                    print("Hatalı giriş yaptınız. Lütfen sadece rakam giriniz.")

            sifre=input(print("Lütfen şifrenizi giriniz:"))
            print("\nSİSTEME GİRİŞ YAPILDI!!! \n\n")
                
        #eposta adresiyle giriş yapma
        elif giris_secim=="8":
            e_posta=input(print("Lütfen e-posta adresinizi giriniz:"))
            sifre=input(print("Lütfen şifrenizi giriniz:"))
            print("\nSİSTEME GİRİŞ YAPILDI!!! \n\n")
                
        else:
            print("Geçersiz seçim yaptınız. Lütfen tekrar deneyin.")
              
            

    #şifremi unuttum ile tel no ya da eposta adresiyle şifer değiştirme
    elif secim==3:
        print("-ŞİFREMİ UNUTTUM-")
        sifremi_unuttum=input(print(""""Şifrenizi unuttunuz ve değiştirmek mi istiyorsunuz? 
                                    Şİfrenizi telefon numarası ile değiştirmek için 4'e, e-posta
                                    adresi ile değiştirmek için 5'ye basınız:"""))
        #tel no ile şifre değiştirme. telefona gelen kodu girerek yeni şifre oluşturma
        if sifremi_unuttum=="4":
            while True: #tel no da sadece rakam girişi yapma
                tel_no=input(print("Telefon numaranızı giriniz:"))
                if tel_no.isdecimal():
                    break
                else:
                    print("Hatıl giriş yaptınız. Lütfen sadece rakam giriniz.")   
                
            kod=input(print("Telefonunuza gelen kodu giriniz:"))
            yeni_sifre=input(print("Yeni şifrenizi giriniz:"))
            print("\nŞİFRENİZ DEĞİŞTİRİLDİ!!! \n\n")
                
        #eposta ile şifre değiştirme. epostaya gelen kodu girerek yeni şifre oluşturma
        elif sifremi_unuttum=="5":
            e_posta=input(print("Lütfen e-posta adresinizi giriniz:"))
            kod=input(print("E-posta adresinize gelen kodu giriniz:"))
            yeni_sifre=input(print("Yeni şifrenizi giriniz:"))
            print("\nŞİFRENİZ DEĞİŞTİRİLDİ!!! \n\n")
                
        else:
            print("Geçersiz seçim yaptınız. Lütfen tekrar deneyin.")
            
      
#admin olarak mı kullanıcı olarak mı giriş yapılacağının seçimi
giris=input(print(""""Sisteme admin olarak mı giriş yapmak istiyorsunuz kullanıcı olarak mı giriş
                  yapmak istiyorsunuz: """))
if giris.lower()=="admin":
    print("-ADMİN GİRİŞİ-")
    admin_girisi()
    
    kullanici_adi_gir = input("Erişmek istediğiniz kullanıcının bilgileri için kullanıcı adı giriniz: ")

    kullanici_bilgileri = {"kullanici adi": kullanici_adi,
                           "adi_soyadi": ad_soyadi,
                           "telefon_numarasi": telefon_no,
                           "eposta_adresi": eposta,
                           "TC_numarasi": tc_no,
                           "adres": adres,
                           "sifre": sifre}   

    print("Kullanıcı Bilgileri:")
    print("Kullanıcı Adı:", kullanici_bilgileri["kullanici adi"])
    print("Adı ve Soyadı:", kullanici_bilgileri["adi_soyadi"])
    print("Telefon Numarası:", kullanici_bilgileri["telefon_numarasi"])
    print("Email:", kullanici_bilgileri["eposta_adresi"])
    print("TC Numarası:", kullanici_bilgileri["TC_numarasi"])
    print("Adres:", kullanici_bilgileri["adres"])
    print("Şifre:", kullanici_bilgileri["sifre"])
    

elif giris.lower()=="kullanıcı":
    print("-KULLANICI GİRİŞİ-")
    kullanici_girisi()
    GirisMetni=(""""Uygulamaya hoş geldiniz Bu uygulama, deprem anında ve depremden sonrasında
                size yardım etmek için vardır. Deprem sırasında depreme yakalandığınız yeri ve
                sağlık durumunuzu girerek yardım çağırabilirsiniz. Depremden sonra ise maddi ve
                manevi yardım için başvurular yapabilirsiniz. \n""")
    print(GirisMetni)
    
    secim2=input("deprem sırasındaki işlemler için 1'e depremden sonraki işlemler için 2'ye basınız")
    if secim2=="1":
        adres=input("Merhaba!!! Adresiniz sisteme kayıtlı mı? (Evetse 'E'ye, hayirsa 'H'ye basiniz) \n")
        if adres.upper()=="E":
            print("Adresiniz kayıtlıdır. Devam edebilirsiniz")
        else:
            adres=input("Adresinizi giriniz: \n")

        apartman_adi=input("Apartman adını giriniz: \n")
        kat_no=input("Kat numarasını giriniz: \n")
        daire_no=input("Daire numaranızı giriniz: \n")
        oda=input("Hangi odada olduğunuzu giriniz: \n")
        yakin_tel_no=int(input("Yakın bir tanıdığınızın telefon numarasını giriniz:"))
        saglik_durumu=input("Lütfen sağlık durumunuz hakkında bize birkaç bilgi veriniz:")
        yaninizda_biri_var_mi=input("yaninizda biri var mi? (Evetse 'E'ye, Hayirsa 'H'ye basiniz)")
        if yaninizda_biri_var_mi.upper()=="E":
            yaninizdaki_kisinin_saglik_durumu = input("Yanınızdaki kişinin sağlık durumunu nedir?: ")
        
        
        print(adres)
        print(apartman_adi)
        print(kat_no)
        print(daire_no)
        print(oda)
        print(yakin_tel_no)
        print(saglik_durumu)
        print(yaninizda_biri_var_mi)
        print(yaninizdaki_kisinin_saglik_durumu)
 
    if secim2=="2":
        ev_hasar_durumu = input("Evinizin hasar durumu: ")
        yardim_kurumlari=("AFAD","YEŞİLAY", "KIZILAY", "AHBAP")
        print(yardim_kurumlari)
        yardim_kurum_sec=input("Yardım almak istediğiniz kurumları seçiniz:")
        yardim_tipi=input("nasıl bir yardım almak istediğinizi giriniz:")
        su_anki_adresiniz=input("Şu anda yaşadığınız yerin adresini giriniz:")
        print("Yardım talebiniz başarıyla gerçekleşmiştir.")


else:
    print("Geçersiz giriş seçimi yaptınız. lütfen tekrardan deneyiniz!!!")

