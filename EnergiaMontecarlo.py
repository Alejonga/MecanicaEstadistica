import numpy as np
import matplotlib.pyplot as plt
 
matrizaux = np.zeros((10, 10), dtype=int)
matriz = matrizaux+1
n = len(matriz[:, 0])

#Creación spines aleatoreos
for l in range(n):
    for m in range(n):
        matriz[l, m] = matriz[l, m]-2*np.random.randint(0, 2)

#Función de energia
def Energia(matriz):
    suma=0
    n=len(matriz[:,0])
    for i in range(n):
        for j in range(n):
            index=matriz[i,j]
            #hacia arriba
            if i>0:
                product1=index*matriz[i-1,j]
                suma=suma+product1
            #hacia abajo
            if i<n-1:
                product2=index*matriz[i+1,j]
                suma=suma+product2
            #hacia izquierda
            if j>0:
                product3=index*matriz[i,j-1]
                suma=suma+product3
            #hacia derecha
            if j<n-1:
                product4=index*matriz[i,j+1]
                suma=suma+product4
    return suma / 2

#Función de magnetización
def Magnetizacion(matriz):
    result=np.sum(matriz)
    return result

#Paso de Metropolis-Montecarlo
def Metropolis(matriz, j, beta):

    #Escogemos un fila y columna aleatoria
    faleatorea = np.random.randint(0,n)
    caleatorea = np.random.randint(0,n)
    
    #Calculamos energia actual
    inicial=-j*Energia(matriz)
    
    #Invertimos el spin
    matriz[faleatorea,caleatorea]=-matriz[faleatorea,caleatorea]
    
    #Calculamos eneriga final
    final=-j*Energia(matriz)
    
    #Calculamos el delta
    delta=inicial-final
    
    #Criterio de aceptación
    if delta>0 and np.random.random() > np.exp(-delta * beta):
       matriz[faleatorea,caleatorea]=-matriz[faleatorea,caleatorea]
    return matriz


#Definición parametros de Montecarlo
numero_pasos=10000
energias = []
magnetizaciones = []
j= 1
beta= 0.5

#Simulación Montecarlo
for paso in range(numero_pasos):

    #Aplicamos paso de montecarlo
    arreglo = Metropolis(matriz, j, beta)

    #Calculamos energia y magnetización
    energia = Energia(arreglo)
    magnetizacion = Magnetizacion(arreglo)

    #Almacenamos resultados
    energias.append(energia)
    magnetizaciones.append(magnetizacion)   

#Grafica

# Crear una lista de números de pasos de Montecarlo (1, 2, 3, ...)
num_pasos = list(range(1, len(energias) + 1))

# Crear el gráfico
plt.plot(num_pasos, energias, label='Energía')
plt.xlabel('Número de Pasos de Montecarlo')
plt.ylabel('Energía')
plt.title('Evolución de la Energía en la Simulación de Montecarlo')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()

#Calcular energia y magnetización promedio
promedio_energias = sum(energias) / len(energias)
promedio_magnetizaciones = sum(magnetizaciones) / len(magnetizaciones)
print("Promedio Energia: ", promedio_energias)
print("Promedio Magnetización: ", promedio_magnetizaciones)


