class Calisan:
    zam_orani = 1.3
    def __init__(self,isim,soyad,maas):
        self.isim = isim
        self.soyad = soyad
        self.maas = maas
        self.email = isim + soyad + "@sirket.com"
    
    def info(self):
        return "Ad: {} Soyad: {} Maaş: {} Email: {}".format(self.isim,self.soyad,self.maas,self.email)

calisan1 = Calisan("Varol","Parlak",3800)
calisan2 = Calisan("Enes","Parlak",5000)

class Yazilimci(Calisan):
    
    def __init__(self, isim, soyad, maas,lang):
        super().__init__(isim, soyad, maas)
        self.lang = lang

    def info(self):
        return "Ad: {} Soyad: {} Maaş: {} Email: {} Bildiği Dil: {}".format(self.isim,self.soyad,self.maas,self.email,self.lang)
    
    
    
yazilimci1 = Yazilimci("Engin","Can",25000,"Python")
yazilimci2 = Yazilimci("Buğra","Han",14000,"C#")

class Yonetici(Calisan):
    def __init__(self, isim, soyad, maas, calisanlar = None):
        super().__init__(isim, soyad, maas)
        if calisanlar == None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar

    def calisan_ekle(self,calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)

    def calisan_sil(self,calisan):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)

    def calisan_goster(self):
        print(f"{self.isim} Altında Çalışanlar: " )
        for calisan in self.calisanlar:
            print(calisan.info())


yonetici1 = Yonetici("Galip","Can",1200)

yonetici1.calisan_ekle(calisan1)
yonetici1.calisan_ekle(yazilimci1)

yonetici1.calisan_goster()