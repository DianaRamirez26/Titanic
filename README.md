# Análisis exploratorio del dataset Titanic

## Descripción del proyecto

Este proyecto realiza un análisis exploratorio del dataset Titanic utilizando Python y pandas. El propósito es explorar las características de los pasajeros, realizar un tratamiento básico de los datos faltantes y analizar diferentes factores relacionados con la supervivencia.

## Fuente de los datos

El dataset utilizado corresponde al conjunto de datos Titanic disponible en Kaggle, utilizando principalmente el archivo `train.csv`.

El dataset contiene información de 891 pasajeros y 12 variables originales relacionadas con características como edad, sexo, clase del pasajero, tarifa, familiares y supervivencia.

## Objetivo

Realizar un análisis exploratorio del dataset Titanic para identificar patrones en los datos y observar cómo se distribuye la supervivencia de los pasajeros de acuerdo con diferentes características.

## Requisitos

Para ejecutar el proyecto se necesita:

- Python 3
- pandas
- matplotlib

Las dependencias utilizadas se encuentran en el archivo `requirements.txt`.

## Instalación

Se recomienda utilizar un entorno virtual para mantener separadas las dependencias del proyecto.

Crear el entorno virtual:

python3 -m venv .venv

## Activar el entorno virtual en Ubuntu/Linux:

source .venv/bin/activate

## Instalar las dependencias:

pip install -r requirements.txt

## Ejecución

Con el entorno virtual activado y ubicándose en la carpeta principal del proyecto, ejecutar:

python src/analysis.py

El programa carga el archivo data/train.csv, realiza la exploración y el procesamiento de los datos, muestra los resultados en la terminal y genera las visualizaciones.

Las imágenes generadas se guardan en:

outputs/resultados/

## Exploración y procesamiento

Durante el análisis inicial se revisaron:

Dimensiones del dataset.
Nombres de las columnas.
Tipos de datos.
Valores faltantes.
Registros duplicados.
Estadísticas descriptivas.
Distribución de la variable Embarked.
Estadísticas de la variable Age.

## Tratamiento de valores faltantes

La variable Age presentó 177 valores faltantes. Para completar estos valores se utilizó la mediana de la variable.

La variable Embarked presentó 2 valores faltantes. Estos fueron reemplazados utilizando la categoría con mayor frecuencia.

La variable Cabin presentó una cantidad considerable de valores faltantes. En lugar de intentar completar los valores originales, se creó la variable HasCabin, que indica si el pasajero cuenta con información de cabina.

## Nuevas variables

Se crearon las siguientes variables:

FamilySize: Representa el tamaño de la familia que viajaba con el pasajero y se calculó mediante:
FamilySize = SibSp + Parch + 1

Alone: Indica si el pasajero viajaba solo.
0 = viajaba acompañado.
1 = viajaba solo.

HasCabin: Indica si existe información registrada en la columna Cabin.
0 = no tiene información de cabina.
1 = tiene información de cabina.

AgeGroup: Agrupa a los pasajeros de acuerdo con su edad:
Niño: hasta 12 años.
Adolescente: más de 12 hasta 18 años.
Adulto joven: más de 18 hasta 30 años.
Adulto: más de 30 hasta 50 años.
Adulto mayor: más de 50 hasta 80 años.

## Análisis realizados
Se realizaron los siguientes análisis:
Porcentaje general de supervivencia.
Porcentaje de supervivencia según sexo.
Porcentaje de supervivencia según clase del pasajero.
Porcentaje de supervivencia según si viajaba solo o acompañado.
Porcentaje de supervivencia según grupo de edad.

## Resultados principales
El porcentaje general de supervivencia registrado en el dataset fue de 38.38%.

La supervivencia según sexo fue:
Mujeres: 74.20%
Hombres: 18.89%

La supervivencia según clase fue:
Primera clase: 62.96%
Segunda clase: 47.28%
Tercera clase: 24.24%

La supervivencia según si viajaba solo o acompañado fue:
Acompañado: 50.56%
Solo: 30.35%

La supervivencia según grupo de edad fue:
Niño: 57.97%
Adolescente: 42.86%
Adulto joven: 33.11%
Adulto: 42.32%
Adulto mayor: 34.38%

Estos resultados representan porcentajes observados dentro del dataset y no implican por sí mismos una relación causal entre las variables.

## Visualizaciones

El proyecto genera tres visualizaciones principales:

Distribución general de supervivencia.
Porcentaje de supervivencia según sexo.
Porcentaje de supervivencia según clase.

Las visualizaciones se encuentran en:

outputs/resultados/
Conclusiones

El análisis exploratorio permitió identificar diferencias en los porcentajes de supervivencia de los pasajeros según distintas características.

En el dataset analizado, el porcentaje de supervivencia fue diferente entre hombres y mujeres, así como entre las distintas clases de pasajeros. También se observaron diferencias entre pasajeros que viajaban solos y aquellos que viajaban acompañados.

El tratamiento de los valores faltantes permitió trabajar con una versión procesada del dataset sin valores faltantes en Age y Embarked, mientras que para Cabin se utilizó una variable indicadora de disponibilidad de información.

Finalmente, la creación de variables como FamilySize, Alone, HasCabin y AgeGroup permitió ampliar el análisis y facilitar la comparación de diferentes características de los pasajeros.