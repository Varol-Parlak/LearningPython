def islem_sec(islem):
    def toplama(*args):
        return sum(args)
    
    def carpma(*args):
        carpim = 1
        for arg in args:
            carpim *= arg
        return carpim 
    
    def ortalama(*args):
        return sum(args) / len(args)
    
    if islem == "toplama":
        return toplama
    elif islem == "çarpma":
        return carpma
    elif islem == "ortalama":
        return ortalama
    
islem = str(input("İşlem Seçiniz: "))

cevap = islem_sec(islem)

cevap = cevap(2,4,6,7,3)
print(cevap)



def kisi_sec(kisi):
    def takim_sec(takim):
        return f"{kisi} {takim} Takımını Tutuyor"
    return takim_sec
    
a = kisi_sec("Varol")
b = kisi_sec("Enes")

print(a("Beşiktaş"))
print(b("Fenerbahçe"))