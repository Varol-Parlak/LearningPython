# def topla(x,y):
#     return x + y

# def carp(x,y):
#     return x * y

# def islem_yap(fonk,a,b):
#     return fonk(a,b)

# print(islem_yap(carp,2,4))


list1 = [2,4,6,8]
list2 = [1,3,5,7,9]
empty = []
def kare(list):

    for num in list:
        i = num ** 2
        empty.append(i)
    print(empty)

def kup(list):
    for num in list:
        i = num ** 3
        empty.append(i)
    print(empty)

def map(fonk, liste):
    sonuc = fonk(liste)
    return sonuc

map(kup,list2)
  