from es_primo import es_primo
from generar_primos_de_beimar import generar_primos_de_beimar

def verificar_lista_de_primos(primos):
    longitud = len(primos)
    contador_errores = longitud
    for primo in primos:
        if(es_primo(primo) == False):
            contador_errores -= 1
            # print(f"{primo} no es primo :'[")
    porcentaje = int(((longitud-contador_errores)/longitud)*100)
    print(f"la diferencia fue de {(longitud-2)-contador_errores} de {longitud-2}, {porcentaje}% de error")
            
# lista_primos = generar_primos_de_beimar(100) 
# verificar_lista_de_primos(lista_primos)