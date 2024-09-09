from descomponer_en_factores_primos import descomponer_en_factores_primos 
def mostrar_factores_hasta_n(n):
    i = 1
    while n >= i:
        factores = sorted(list(set(descomponer_en_factores_primos(i))))
        print(f"{i} -> {factores}")
        i += 1
        
# mostrar_factores_hasta_n(1000)