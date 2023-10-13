# MecanicaEstadistica
Punto 2 Tarea 3 Mecánica Estadística
Realice la simulación en dos archivos .py diferentes, esto debido a que tuve inconvenientes para unir ambas graficas.
En el archivo llamado EnergiaMontecarlo.py podemos realizar la grafica de la energia en función de los pasos de MonteCarlo,
en donde tenemos la definición de todas las funciones necesarias para realizar nuestra simulación, donde definimos el caluclo
de la energia, la creación de una configuración inicial, la estructuración del paso de montecarlo, para luego aplicar 10000
pasos en nuestra simulación. Al final se calcula y se imprime la energia y magnetización promedio y se grafica energia en función de
los pasos de montecarlo. El archivo EnergiaVsTemperatura.py tiene en principio la misma estructura de funciones usadas en el archivo
anterior con la diferencia de que en este se implementa un ciclo for extra para hacer 10000 pasos de montecarlo por cada una de las 
temperaturas en el rango que deseemos analizar. Importante aclarar que en el archivo EnergiaVsTemperatura se debe tomar un start_temp
que sea diferente a 0, esto debido a que el programa divide por la temperatura. En ambos archivos es posible modificar el tamaño de 
la red por medio del parametro "N" asi como es posible modificar los pasos de montecarlo por medio del parametro "num_pasos". 
