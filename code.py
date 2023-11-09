from ucimlrepo import fetch_ucirepo

# fetch dataset
heart_disease = fetch_ucirepo(id=45)

# data (as pandas dataframes)
X = heart_disease.data.features
y = heart_disease.data.targets

# metadata
print(heart_disease.metadata)

# variable information
print(heart_disease.variables)

import requests
import csv
from io import StringIO

# URL del enlace de la pagina de Heart Disease
url = "https://archive.ics.uci.edu/static/public/45/data.csv"

# Realiza una solicitud GET para obtener la respuesta del servidor
response = requests.get(url)

if response.status_code == 200:
    # Obtén los datos del contenido de la respuesta
    datos_csv = response.text
    # Utiliza StringIO para convertir los datos CSV en un archivo de lectura
    csv_file = StringIO(datos_csv)
    # Utiliza el módulo csv para leer los datos y convertirlos en una lista de listas
    reader = csv.reader(csv_file)
    matriz = [fila for fila in reader]
    matriz = matriz[1:]
    for fila in matriz:
      print(fila)
    # Ahora 'matriz' contiene los datos en formato de lista de listas
else:
    print("No se pudo obtener datos. Código de estado:", response.status_code)

#Creacion de la matriz con los umbrales de edad
Matriz_umbrales_edad = []
for fila in matriz:
    edad = int(fila[0])

    elemento_edad_30 = 1 if edad <= 30 else 0
    elemento_edad_38 = 1 if 30 < edad <= 38 else 0
    elemento_edad_46 = 1 if 38 < edad <= 46 else 0
    elemento_edad_54 = 1 if 46 < edad <= 54 else 0
    elemento_edad_62 = 1 if 54 < edad <= 62 else 0
    elemento_edad_70 = 1 if 62 < edad <= 70 else 0
    elemento_edad_78 = 1 if 70 < edad <= 78 else 0

    Matriz_umbrales_edad.append([elemento_edad_30, elemento_edad_38, elemento_edad_46, elemento_edad_54, elemento_edad_62, elemento_edad_70, elemento_edad_78])
for fila in Matriz_umbrales_edad:
  print(fila)

#Creacion de la matriz con los umbrales de trestbps
Matriz_umbrales_trestbps = []
for fila in matriz:
    trestbps = int(fila[3])

    elemento_trestbps_100 = 1 if trestbps <= 100 else 0
    elemento_trestbps_114 = 1 if 100 < trestbps <= 114 else 0
    elemento_trestbps_128 = 1 if 114 < trestbps <= 128 else 0
    elemento_trestbps_142 = 1 if 128 < trestbps <= 142 else 0
    elemento_trestbps_156 = 1 if 142 < trestbps <= 156 else 0
    elemento_trestbps_170 = 1 if 156 < trestbps <= 170 else 0
    elemento_trestbps_200 = 1 if 170 < trestbps <= 200 else 0

    Matriz_umbrales_trestbps.append([elemento_trestbps_100, elemento_trestbps_114, elemento_trestbps_128, elemento_trestbps_142, elemento_trestbps_156, elemento_trestbps_170, elemento_trestbps_200])
for fila in Matriz_umbrales_trestbps:
  print(fila)

#Creacion de la matriz con los umbrales de chol
Matriz_umbrales_chol = []
for fila in matriz:
    chol = int(fila[4])

    elemento_chol_200 = 1 if chol <= 200 else 0
    elemento_chol_266 = 1 if 200 < chol <= 266 else 0
    elemento_chol_332 = 1 if 266 < chol <= 332 else 0
    elemento_chol_398 = 1 if 332 < chol <= 398 else 0
    elemento_chol_464 = 1 if 398 < chol <= 464 else 0
    elemento_chol_530 = 1 if 464 < chol <= 530 else 0
    elemento_chol_596 = 1 if 530 < chol <= 596 else 0

    Matriz_umbrales_chol.append([elemento_chol_200, elemento_chol_266, elemento_chol_332, elemento_chol_398, elemento_chol_464, elemento_chol_530, elemento_chol_596])
for fila in Matriz_umbrales_chol:
  print(fila)

#Creacion de la matriz con los umbrales de thalach
Matriz_umbrales_thalach = []
for fila in matriz:
    thalach = int(fila[7])

    elemento_thalach_100 = 1 if thalach <= 100 else 0
    elemento_thalach_120 = 1 if 100 < thalach <= 120 else 0
    elemento_thalach_140 = 1 if 120 < thalach <= 140 else 0
    elemento_thalach_160 = 1 if 140 < thalach <= 160 else 0
    elemento_thalach_180 = 1 if 160 < thalach <= 180 else 0
    elemento_thalach_200 = 1 if 180 < thalach <= 200 else 0
    elemento_thalach_220 = 1 if 200 < thalach <= 220 else 0

    Matriz_umbrales_thalach.append([elemento_thalach_100, elemento_thalach_120, elemento_thalach_140, elemento_thalach_160, elemento_thalach_180, elemento_thalach_200, elemento_thalach_220])
for fila in Matriz_umbrales_thalach:
  print(fila)

#Creacion de la matriz con los umbrales de oldpeak
Matriz_umbrales_oldpeak = []
for fila in matriz:
    oldpeak = float(fila[9])

    elemento_oldpeak_0 = 1 if oldpeak <= 0 else 0
    elemento_oldpeak_1 = 1 if 0 < oldpeak <= 1 else 0
    elemento_oldpeak_2 = 1 if 1 < oldpeak <= 2 else 0
    elemento_oldpeak_3 = 1 if 2 < oldpeak <= 3 else 0
    elemento_oldpeak_4 = 1 if 3 < oldpeak <= 4 else 0
    elemento_oldpeak_5 = 1 if 4 < oldpeak <= 5 else 0
    elemento_oldpeak_7 = 1 if 5 < oldpeak <= 7 else 0

    Matriz_umbrales_oldpeak.append([elemento_oldpeak_0, elemento_oldpeak_1, elemento_oldpeak_2, elemento_oldpeak_3, elemento_oldpeak_4, elemento_oldpeak_5, elemento_oldpeak_7])
for fila in Matriz_umbrales_oldpeak:
  print(fila)

#Creacion de la matriz con los umbrales de ca
Matriz_umbrales_ca = []
for fila in matriz:
    ca = float(fila[11])

    elemento_ca_0 = 1 if ca <= 0 else 0
    elemento_ca_05 = 1 if 0 < ca <= 0.5 else 0
    elemento_ca_1 = 1 if 0.5 < ca <= 1 else 0
    elemento_ca_15 = 1 if 1 < ca <= 1.5 else 0
    elemento_ca_2 = 1 if 1.5 < ca <= 2 else 0
    elemento_ca_25 = 1 if 2 < ca <= 2.5 else 0
    elemento_ca_3 = 1 if 2.5 < ca <= 3 else 0

    Matriz_umbrales_ca.append([elemento_ca_0, elemento_ca_05, elemento_ca_1, elemento_ca_15, elemento_ca_2, elemento_ca_25, elemento_ca_3])
for fila in Matriz_umbrales_ca:
  print(fila)

#Pasar las variables categoricas a una matriz para que quede con las mismas dimensiones de las matrices convertidas
import math

Matriz_categoricas = []
for fila in matriz:
  sex = int(fila[1])
  cp = int(fila[2])
  fbs = int(fila[5])
  restecg = int(fila[6])
  exang = int(fila[8])
  slope = int(fila[10])
  if math.isnan(float(fila[12])):
      fila = 0
  else:
    thal = float(fila[12])

  Matriz_categoricas.append([sex, cp, fbs, restecg, exang, slope, thal])

for fila in Matriz_categoricas:
  print(fila)

#Hacer la matriz que contenga todas las matrices una vez modificadas
import numpy as np
Matriz_final = []
Matriz_final = np.concatenate((Matriz_umbrales_edad, Matriz_umbrales_trestbps, Matriz_umbrales_chol, Matriz_umbrales_thalach, Matriz_umbrales_oldpeak, Matriz_umbrales_ca, Matriz_categoricas), axis = 1)
print(Matriz_final.shape)

from sklearn.manifold import MDS

# Crea una instancia del modelo MDS
mds = MDS(n_components=2)  # Asignamos de 2 dimensiones

# Aplica MDS a la matriz final obtenida
nueva_dimension = mds.fit_transform(Matriz_final)
print(nueva_dimension.shape)

import matplotlib.pyplot as plt
import numpy as np
colores = []
num = []

#Llamamos los elementos de la variable Num
for fila in matriz:
  num.append(int(fila[13]))

#Evaluamos los valores de Num para determinar los colores dentro del grafico, luego creamos el grafico
for i in range(303):
    x= nueva_dimension[i,0]
    y= nueva_dimension[i,1]
    colores = ['purple' if num[i] == 0 else 'yellow']
    plt.scatter(x,y, c = colores)

# Insertamos la barra de color con su indicador y le agregamos titulo al grafico para al final mostrarlo
plt.colorbar(label='Heart Disease Diagnosis')
plt.title('Gráfico de Dispersión MDS')
plt.show()
