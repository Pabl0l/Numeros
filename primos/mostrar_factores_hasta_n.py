from descomponer_en_factores_primos import descomponer_en_factores_primos
def mostrar_factores_hasta_n(n):
    i = 1
    while n >= i:
        print(sorted(descomponer_en_factores_primos(i)))
        i += 1

# mostrar_factores_hasta_n(1000)