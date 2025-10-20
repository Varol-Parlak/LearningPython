with open("ornek_metin.txt") as f:
    with open("gecenler.txt","w") as g:
        with open("kalanlar.txt","w") as k:
            icerik = f.readlines()
            for satir in icerik:
                satir = satir.replace("\n","")
                bosluk_sayisi = 0
                bosluk_i = []
                i = 0
                for karakter in satir:
                    if karakter == " ":
                        bosluk_sayisi+=1
                        bosluk_i.append(i)
                    i += 1 
                ad_soyad = satir[:bosluk_i[0]]
                soyad = ad_soyad.split("-")[-1]
                ad = ad_soyad[:ad_soyad.index(soyad) -1]
                ad = ad.replace("-"," ")
                notlar = satir.split(" ")[-1]
                notlar = notlar.split("/")
                vize1 = int(notlar[0])
                vize2 = int(notlar[1])
                final = int(notlar[2])
                ortalama = vize1 * 0.3 + vize2 * 0.3 + final * 0.4 
                bolum = satir[bosluk_i[0] + 1 : bosluk_i[-1]]
                
                if ortalama >= 70 and final >= 70:
                    g.write(ad," " * (25 - len(ad)))
                    g.write(soyad," " * (25 - len(soyad)))
                    g.write(bolum," " * (25 - len(bolum)))
                    g.write(str(round(ortalama , 1))," " * 21)
                    g.write("Passed\n")
                else:
                    k.write(ad," " * (25 - len(ad)))
                    k.write(soyad," " * (25 - len(soyad)))
                    k.write(bolum," " * (25 - len(bolum)))
                    k.write(str(round(ortalama , 1))," " * 21)
                    k.write("Failed\n")    






