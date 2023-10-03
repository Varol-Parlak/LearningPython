import time

def decorator(fonk):
    def wrapper(*args):
        baslangic = time.time()
        fonk(*args)
        bitis = time.time()
        print(f"{bitis - baslangic} süresiyle bitti")
    return wrapper

@decorator
def kare_al(liste):
    sonuc = []
    for num in liste:
        sonuc.append(num**2)
    return sonuc

@decorator
def kup_al(liste):
    sonuc = []
    for num in liste:
        sonuc.append(num**3)
    return sonuc

@decorator
def topla(*args):
    time.sleep(1)
    return sum(args)

topla(1,2,4,5,3,2,4)

