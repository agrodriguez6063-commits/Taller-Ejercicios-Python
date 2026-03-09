import pandas as pd

df = pd.read_csv("data/personas.csv")

# Normalizar campo activo
df["activo"] = (
    df["activo"]
    .astype(str)
    .str.strip()
    .str.lower()
)

# Contar valores falsos
falsos = df["activo"].isin(['false', '0', 'no']).sum()

print(f"Existen {falsos} registros con 'activo' como falso.")