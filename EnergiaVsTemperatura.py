import numpy as np
import matplotlib.pyplot as plt

# Función de espines aleatoreos
def configuracion_inicial(N):   
    state = 2*np.random.randint(2, size=(N,N))-1
    return state

#Funcion de energia
def Energia(matriz):
    suma = 0
    n = len(matriz[:, 0])
    for i in range(n):
        for j in range(n):
            index = matriz[i, j]
            neighbor_sum = matriz[(i + 1) % n, j] + matriz[i, (j + 1) % n] + matriz[(i - 1) % n, j] + matriz[i, (j - 1) % n]
            suma += -index * neighbor_sum  
    return suma / 4  

#Funcion de magnetizacion
def Magnetizacion(matriz):
    mag=np.sum(matriz) / (N * N)
    return mag

#Definimos paso de montecarlo
def paso_monte_carlo(matriz, temperatura):
    energia_inicial = 0
    energia_final = 0
    s = 0
    i, j = np.random.randint(0, N, 2)  
    s = matriz[i, j]  
    energia_inicial = Energia(matriz)
    matriz[i, j] = -s  # Invertir el espín
    energia_final = Energia(matriz)
    
    deltaE = energia_final - energia_inicial
    if deltaE <= 0 or np.random.random() < np.exp(- (0.5 * np.log(1+(2**(0.5))) * deltaE ) / (temperatura)):
        pass
    else:
        matriz[i, j] = s
    return matriz
#Parametros iniciales
N=10
config = configuracion_inicial(N)
num_pasos = 10000
magnetizaciones_promedio = []
start_temp = 0.02
end_temp = 1.5
temp_step = 0.02
rango_temperatura = np.arange(start_temp, end_temp + temp_step, temp_step)

# Realizamos los pasos de Monte Carlo promediando en cada temperatura
for temperatura in rango_temperatura:
    configuracion=configuracion_inicial(N)
    energias = []
    magnetizaciones = []

    for paso in range(num_pasos):
        paso_monte_carlo(config, temperatura)
        energia_actual = Energia(config)
        energias.append(energia_actual)
        magnetizacion_actual = Magnetizacion(config)
        magnetizaciones.append(magnetizacion_actual)

    magnetizaciones_promedio.append(np.mean(magnetizaciones[-4000:]))

# Crear el gráfico
plt.scatter(rango_temperatura, magnetizaciones_promedio)
plt.xlabel('T/Tc')
plt.ylabel('Magnetización')
plt.title('Magnetización vs Temperatura')
plt.grid(True)

# Mostrar el gráfico
plt.show()