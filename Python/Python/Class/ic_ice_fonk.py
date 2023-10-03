# def calc(x):
#     def kare_al(a):
#         return a ** 2
#     def karekok_al(a):
#         return a ** 0.5
#     def faktoriyel(a):
#         carpim = 1
#         for i in range(1, a + 1):
#             carpim *= i 
#         return carpim
#     kare = kare_al(x)
#     karekok = karekok_al(x)
#     fakt = faktoriyel(x)
#     return f"Karesi: {kare}, Karekökü: {karekok}, Faktöriyeli: {fakt}"
    
# print(calc(4))

def toplam_carp(*args):
    def toplama(demet):
        return sum(demet)
    def carpma(demet):
        carpim = 1
        for i in demet:
            carpim *= i
        return carpim
    return f"Toplamları: {toplama(args)} Carpımları: {carpma(args)}"


print(toplam_carp(2,6,3,4,6))