from generar_numeros_primos_hasta_n import generar_numeros_primos_hasta_n
import matplotlib.pyplot as plt
def graficar_numeros_primos_hasta_n(num):
    # Importamos la biblioteca matplotlib.pyplot para crear gráficos

    # Definimos la lista de primos
    primos = generar_numeros_primos_hasta_n (num) # primos

    # Generamos los índices automáticamente
    indices = list(range(1, len(primos) + 1))

    # Creamos la gráfica
    plt.plot(indices, primos,
         marker='o',        # Marcador de punto circular
         linestyle='--',    # Línea discontinua
         color='m',         # Color magenta
         linewidth=0.2,       # Grosor de la línea
         markersize=1,      # Tamaño de los marcadores
         alpha=0.7,         # Transparencia de la línea
         label='Primos')

    # Añadimos título y etiquetas a los ejes
    plt.title('primos vs. i')
    plt.xlabel('i')
    plt.ylabel('Primos')

    # Añadimos una leyenda para la gráfica
    plt.legend()

    # Mostramos la gráfica
    plt.show()

graficar_numeros_primos_hasta_n(10000)