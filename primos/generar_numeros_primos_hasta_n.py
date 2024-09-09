from es_primo import es_primo
def generar_numeros_primos_hasta_n(n):
    # Hallar números primos menores que n
    primos = []
    primo = 2
    while primo <= n:
        if primo == 2:
            primos.append(primo)
            primo += 1
            continue
        if es_primo(primo):
            primos.append(primo)
        primo += 2
    return primos

# print(generar_numeros_primos_hasta_n(1100))