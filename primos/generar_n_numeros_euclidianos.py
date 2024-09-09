from generar_primo_n_euclidiano import generar_primo_n_euclidiano
from es_primo import es_primo

def generar_n_numeros_euclidianos(n):
    numeros_euclidianos = []
    i = 0
    while(i < n):
        primos_euclidianos = generar_primo_n_euclidiano(i)
        numeros_euclidianos.append(primos_euclidianos)
        print( f"numeros euclidianos = {primos_euclidianos} Es primo? = {es_primo(primos_euclidianos)}")
        i += 1
    return numeros_euclidianos

# generar_n_numeros_euclidianos(9)