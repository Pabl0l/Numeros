from generar_numeros_primos_hasta_n import generar_numeros_primos_hasta_n
def cantidad_de_primos_por_debajo_de_n(num):
    primos = generar_numeros_primos_hasta_n(num)
    cantidad = num
    longitud = len(primos)
    for primo in primos:
        entero = int(cantidad / primo)
        cantidad = cantidad - entero + 1
        if(cantidad/primo <= 1):
            cantidad -= 1
            break
    print(f" esperado : {longitud} , recibido : {cantidad}, porcentaje de error: {round(((1-cantidad/longitud)*100),2)}%, porcentaje de primos: {round((longitud*100/num),2)}%")
    return cantidad

# amount = 2 # 1              // 1 -> 50%
# amount = 3 # 1              // 2 -> 66,6%
# amount = 5 # 1              // 3 -> 60%
# amount = 10 # 1              // 4 -> 40%
# amount = 25 # 1              // 9 -> 36%
# amount = 50 # 1              // 15 -> 30%
# amount = 75 # 1              // 21 -> 28%


# amount = 10 # 1                   // 4 -> 40%
# amount = 100 # 1                  // 25 -> 25%
# amount = 101 # 0.88               // 26 -> 25,7%
# amount = 1000 #0.68               // 168 -> 16,8%
# amount = 10000 #0.4579            //  1229 -> 12,29%
# amount = 100000 #0.3405           // 9592 -> 9,59%
# amount = 1000000 #0.26458535      //  78498 -> 7,85%
# amount = 10000000 #0.21458535     // 664579 -> 6,65%
# amount = 100000000 #0.20458535    // 5761455 -> 5,76%

# cantidad_de_primos_por_debajo_de_n(10)