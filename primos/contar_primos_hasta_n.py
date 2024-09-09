from generar_numeros_primos_hasta_n import generar_numeros_primos_hasta_n
def contar_primos_hasta_n(num):
    primos = generar_numeros_primos_hasta_n(num)
    cuenta = len(primos)
    print(f"Hay {cuenta} primos por debajo de {num}, es el {round(cuenta*100/num,2)}%")
    return cuenta

contar_primos_hasta_n(10)