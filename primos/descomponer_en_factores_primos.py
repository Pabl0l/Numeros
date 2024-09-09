from generar_numeros_primos_hasta_n import generar_numeros_primos_hasta_n
from es_primo import es_primo

def descomponer_en_factores_primos(num):
    if(es_primo(num)):
        # print(f"El numero {num} es primo")
        factores = [num]
    elif(num == 1):
        factores = [num]
    else:
        mitad = int(num/2)
        # print("Raiz: ", raiz)
        primos = generar_numeros_primos_hasta_n(mitad)
        
        # print("primos hasta raiz: ", primos)
        factores = []
        for primo in primos:
            if(num%primo == 0):
                division = num / primo
                factores.append(primo)
                while (division % primo == 0):
                       factores.append(primo)
                       division /= primo
        if len(factores) == 1:
            pareja = int(num / factores[0])
            factores.append(pareja)
    return factores

# print(descomponer_en_factores_primos(13))