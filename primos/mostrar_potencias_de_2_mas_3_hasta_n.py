from descomponer_en_potencias import descomponer_en_potencias
from generar_numeros_primos_hasta_n import generar_numeros_primos_hasta_n
def mostrar_potencias_de_2_mas_3_hasta_n(num):
    primos = generar_numeros_primos_hasta_n(num)
    for primo in primos:
        print(descomponer_en_potencias(primo))
     
mostrar_potencias_de_2_mas_3_hasta_n(1000)