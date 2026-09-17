import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("outputs/resultados", exist_ok=True)

# Cargar el dataset
df = pd.read_csv("data/train.csv")

# Mostrar las primeras filas
print(df.head())

# Mostrar dimensiones
print("\nDimensiones del dataset:")
print(df.shape)

# Mostrar nombres de las columnas
print("\nColumnas:")
print(df.columns.tolist())

# Información general del dataset
print("\nInformación del dataset:")
df.info()

# Cantidad de valores faltantes
print("\nValores faltantes por columna:")
print(df.isnull().sum())

df.isnull().sum()

# Revisar registros duplicados
print("\nRegistros duplicados:")
print(df.duplicated().sum())

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe())

# Porcentaje de valores faltantes
print("\nPorcentaje de valores faltantes:")
missing_percentage = df.isnull().mean() * 100
print(missing_percentage)

# Valores de la variable Embarked
print("\nValores de Embarked:")
print(df["Embarked"].value_counts(dropna=False))

# Estadísticas de la variable Age
print("\nEstadísticas de Age:")
print(df["Age"].describe())

# Tratamiento de valores faltantes en Age
df["Age"] = df["Age"].fillna(df["Age"].median())

print("\nValores faltantes en Age después del tratamiento:")
print(df["Age"].isnull().sum())

# Tratamiento de valores faltantes en Embarked
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("\nValores faltantes en Embarked después del tratamiento:")
print(df["Embarked"].isnull().sum())

# Crear indicador de disponibilidad de Cabin
df["HasCabin"] = df["Cabin"].notnull().astype(int)

print("\nVariable HasCabin:")
print(df["HasCabin"].value_counts())
# Crear variable FamilySize
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

print("\nVariable FamilySize:")
print(df["FamilySize"].describe())

# Crear variable Alone
df["Alone"] = (df["FamilySize"] == 1).astype(int)

print("\nVariable Alone:")
print(df["Alone"].value_counts())

# Crear variable AgeGroup
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 12, 18, 30, 50, 80],
    labels=["Niño", "Adolescente", "Adulto joven", "Adulto", "Adulto mayor"]
)

print("\nVariable AgeGroup:")
print(df["AgeGroup"].value_counts().sort_index())

# Mostrar algunas filas con las nuevas variables
print("\nNuevas variables:")
print(df[[
    "SibSp",
    "Parch",
    "FamilySize",
    "Alone",
    "HasCabin",
    "AgeGroup"
]].head(10))

# Análisis 1: porcentaje general de supervivencia
survival_rate = df["Survived"].mean() * 100

print("\nPorcentaje general de supervivencia:")
print(f"{survival_rate:.2f}%")

# Análisis 2: supervivencia según sexo
survival_by_sex = df.groupby("Sex")["Survived"].mean() * 100

print("\nPorcentaje de supervivencia según sexo:")
print(survival_by_sex)

# Análisis 3: supervivencia según clase
survival_by_class = df.groupby("Pclass")["Survived"].mean() * 100

print("\nPorcentaje de supervivencia según clase:")
print(survival_by_class)

# Análisis 4: supervivencia según si viajaba solo o acompañado
survival_by_alone = df.groupby("Alone")["Survived"].mean() * 100

print("\nPorcentaje de supervivencia según si viajaba solo:")
print(survival_by_alone)

print("\nInterpretación de Alone:")
print("0 = viajaba acompañado")
print("1 = viajaba solo")

# Análisis 5: supervivencia según grupo de edad
survival_by_age_group = df.groupby("AgeGroup", observed=True)["Survived"].mean() * 100

print("\nPorcentaje de supervivencia según grupo de edad:")
print(survival_by_age_group)

# Comprobar dimensiones después del procesamiento
print("\nDimensiones después del procesamiento:")
print(df.shape)


# Visualización 1: porcentaje general de supervivencia
survival_counts = df["Survived"].value_counts()

plt.figure(figsize=(6, 4))
plt.bar(["No sobrevivió", "Sobrevivió"], survival_counts[[0, 1]])
plt.title("Distribución de supervivencia")
plt.ylabel("Número de pasajeros")
plt.tight_layout()

plt.savefig("outputs/resultados/supervivencia_general.png")
plt.show()
plt.close()

# Visualización 2: supervivencia según sexo
plt.figure(figsize=(6, 4))
plt.bar(survival_by_sex.index, survival_by_sex.values)
plt.title("Porcentaje de supervivencia según sexo")
plt.xlabel("Sexo")
plt.ylabel("Porcentaje de supervivencia")
plt.ylim(0, 100)
plt.tight_layout()

plt.savefig("outputs/resultados/supervivencia_por_sexo.png")
plt.show()
plt.close()

# Visualización 3: supervivencia según clase
plt.figure(figsize=(6, 4))
plt.bar(
    survival_by_class.index.astype(str),
    survival_by_class.values
)
plt.title("Porcentaje de supervivencia según clase")
plt.xlabel("Clase del pasajero")
plt.ylabel("Porcentaje de supervivencia")
plt.ylim(0, 100)
plt.tight_layout()

plt.savefig("outputs/resultados/supervivencia_por_clase.png")
plt.show()
plt.close()