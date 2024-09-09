from generar_factorial_de_primos_hasta_n import generar_factorial_de_primos_hasta_n

def suma_de_reciprocos_de_primos(num):
    reciproco = 0
    factoriales = generar_factorial_de_primos_hasta_n(num)
    print(factoriales)
    
    for factor in factoriales:
        reciproco += 1/factor
    print(reciproco)
    return reciproco

    
suma_de_reciprocos_de_primos(10)  # = 0.705230171791801 aprox (número más grande que me puede dar python)  # = 70.523% de los números NO son primos
                                  # Se puede concluir que el 29.477% de los números son primos según este cálculo