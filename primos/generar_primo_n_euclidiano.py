from generar_n_numeros_primos import generar_n_numeros_primos

def generar_primo_n_euclidiano(n):
    lista_n_numeros_primos = generar_n_numeros_primos(n)
    # print(lista_n_numeros_primos)
    numero_np_euclidiano = 1
    
    for numero_primo in lista_n_numeros_primos:
        numero_np_euclidiano = numero_primo * numero_np_euclidiano
    return numero_np_euclidiano + 1


print(generar_primo_n_euclidiano(101))

# Primo_oliverino
# def generar_primo_n_euclidiano(n):
#     lista_n_numeros_primos = generar_n_numeros_primos(n)
#     numero_np_euclidiano = 1
#     for numero_primo in lista_n_numeros_primos:
#         numero_np_euclidiano = numero_primo * numero_np_euclidiano + 1  # aquí se van multilplicando los primos de euclides para dar un primo de olivera    
#     return 
