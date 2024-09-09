def potencias_de_2_mas_3(num):
    potencias = [2,3]
    i = 1
    potencia=0
    while i <= num:
        potencia = 2**i + potencia
        potencias.append(potencia+3)
        i += 1
        
    return potencias

# print(potencias_de_2_mas_3(3))