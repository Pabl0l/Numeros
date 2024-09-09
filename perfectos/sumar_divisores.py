from divisores_de_n import divisores_de_n
def sumar_divisores(num):
    lista = divisores_de_n(num)
    total = 0
    for i in lista:
        total += i
    return int(total-num)

# print("100: ", sumar_divisores(100))