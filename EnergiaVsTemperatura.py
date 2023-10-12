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
def Metropolis(matriz, j, temperatura):

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
    if delta>0 and np.random.random() > np.exp(-delta / temperatura):
       matriz[faleatorea,caleatorea]=-matriz[faleatorea,caleatorea]
    return matriz


#Definición parametros de Montecarlo
numero_pasos=10000
energias = []
magnetizaciones = []
j= 1
start = 0
stop = 100
step = 0.1
float_range = np.arange(start, stop, step)

#Simulación Temperatura
for temperatura in float_range:

    #Aplicamos paso de montecarlo
    arreglo = Metropolis(matriz, j, temperatura)

    #Calculamos energia y magnetización
    energia = Energia(arreglo)
    magnetizacion = Magnetizacion(arreglo)

    #Almacenamos resultados
    energias.append(energia)
    magnetizaciones.append(magnetizacion) 

# Crear el gráfico
plt.plot(float_range, magnetizaciones, label='Magnetización')
plt.xlabel('Beta')
plt.ylabel('Magnetización')
plt.title('Magnetización vs Temperatura')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()