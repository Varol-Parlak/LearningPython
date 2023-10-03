from datetime import date

class Stajyer:
    stajyer_sayisi = 0
    def __init__(self,isim,yas):
        self.isim = isim
        self.yas = yas
        Stajyer.stajyer_sayisi += 1 

    def info(self):
        print(f"Ad: {self.isim} Yaş: {self.yas}")
    
    @classmethod
    def stajyer_sayi(cls):
        print(Stajyer.stajyer_sayisi)

    @classmethod
    def string_olus(cls,str_):
        isim,yas = str_.split("-")
        return cls(isim,yas)

    @classmethod 
    def birthday(cls,isim,dogumyili):
        return cls(isim, date.today().year - dogumyili)

    @staticmethod
    def yas_hesap(Stajyer):
        return date.today().year - Stajyer.yas
    
