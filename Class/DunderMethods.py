class Listem(list):
    def __add__(self,other):
        if len(self) != len(other):
            return "Toplanamaz"
        else:
            result = Listem()
            for i in range(len(self)):
                result.append(self[i] + other[i])
        return result

liste1 = Listem([1,2,3])
liste2 = Listem([4,5,6])
print(liste1 + liste2)

class Futbolcu:
    def __init__(self,isim,soyad,yas):
        self.isim = isim
        self.soyad = soyad
        self.yas = yas
    
    def __eq__(self,other):
        if self.isim == other.isim and self.soyad == other.soyad :
            return True
        return False
    
    def __add__(self,other):
        isim = self.isim[0] + other.isim[0]
        soyad = self.soyad[0] + other.soyad[0]
        yas = self.yas + other.yas
        return Futbolcu(isim,soyad,yas)

    def __lt__(self,other):
        if self.yas < other.yas:
            return True
        return False
    
    def __gt__(self,other):
        if self.yas > other.yas:
            return True
        return False
    

futbolcu1 = Futbolcu("Ali","Yalçın",17)
futbolcu2 = Futbolcu("Mehmet","Yalçın",18)

futbolcu3 = futbolcu1 < futbolcu2
print(futbolcu3)