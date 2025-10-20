def asalMi(number, dizi):
    if dizi[0] == number:
        return True
    else:
        adim = dizi[0]
        for i in range(len(dizi) - 1, 0,-1):
            if dizi[i] % adim == 0:
                del dizi[i]
    
    if number not in dizi:
        return False
    return asalMi(number, dizi[1:])


number = int(input("Bir Sayı Giriniz: "))
dizi = list()
for i in range(2, number + 1):
    dizi.append(i)

if asalMi(number, dizi):
    print(f"{number} sayısı asaldır")
else:
    print(f"{number} sayısı asal değildir")

