from generar_numeros_primos_hasta_n import generar_numeros_primos_hasta_n

def generar_factorial_de_primos_hasta_n(num):
    primos = generar_numeros_primos_hasta_n(num)
    compuestos = []
    compuesto_actual = 1
    for primo in primos:
        compuesto_actual *= primo
        compuestos.append(compuesto_actual)
    return compuestos

# print(generar_factorial_de_primos_hasta_n(11))