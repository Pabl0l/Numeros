def descomponer_en_potencias(numero_primo):
    potencias = []  # Lista para almacenar las potencias de 3 y 2
    n = numero_primo  # Número inicial

    # Determinar la mayor potencia de 3
    potencia_3 = 1  # Iniciamos con 3**0
    while 3 ** (potencia_3 + 1) <= n:
        potencia_3 += 1

    # Agregar la mayor potencia de 3 posible y restarla del número
    while potencia_3 >= 1:
        if 3 ** potencia_3 <= n:
            potencias.append(f"3**{potencia_3}")
            n -= 3 ** potencia_3
        potencia_3 -= 1

    # Determinar la mayor potencia de 2
    potencia_2 = 1  # Iniciamos con 2**0
    while 2 ** (potencia_2 + 1) <= n:
        potencia_2 += 1

    # Agregar la mayor potencia de 2 posible y restarla del número
    while potencia_2 >= 1:
        if 2 ** potencia_2 <= n:
            potencias.append(f"2**{potencia_2}")
            n -= 2 ** potencia_2
        potencia_2 -= 1

    return f"{numero_primo}  =  {potencias}"


# print(descomponer_en_potencias(541))
# print(descomponer_en_potencias(509))
# print(descomponer_en_potencias(499))