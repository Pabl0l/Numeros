from sumar_divisores import sumar_divisores
from divisores_de_n import divisores_de_n
def bucle_sumar_divisores_hasta_n(num):
    i = 1
    while i <= num:
        total = sumar_divisores(i)
        if i < total:
            es = "MAYOR"
            print(f"{i} : {total} -> {divisores_de_n(i)}")
        elif i==total:
            es = "igual"
        else:
            es = "menor"
        # print(f"{i} : {total}, la suma es {es}")
        i += 1

bucle_sumar_divisores_hasta_n(496)