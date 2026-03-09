import pandas as pd

df = pd.read_csv("data/personas.csv")

# Limpiar la columna salario
df["salario"] = (
    df["salario"]
    .astype(str)
    .str.replace(",", ".", regex=False)      # convertir coma decimal a punto
    .str.replace(r"[^\d.]", "", regex=True)  # eliminar todo excepto números y punto
)

# Convertir a número
df["salario"] = pd.to_numeric(df["salario"], errors="coerce")

# Calcular el promedio
promedio = df["salario"].mean()

print(f"El salario promedio después de limpiar es: {promedio:.2f}")