from generar_numeros_primos_hasta_n import generar_numeros_primos_hasta_n
def mostrar_diferencia_entre_primos_hasta_n(n):
    if(n>2):
        diferencias = []
        primos = generar_numeros_primos_hasta_n(n)
        i = 0
        while (len(primos)+1>i):
            if(primos[i+1] != primos[-1]):
                diferencias.append(primos[i+1] - primos[i])
                i +=1
            else:
                break
    else:
        print("ingrese un numero mayor a 2.")
    return diferencias
# print(mostrar_diferencia_entre_primos_hasta_n(1010))