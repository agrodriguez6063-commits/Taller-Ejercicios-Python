import pandas as pd

df = pd.read_csv("data/personas.csv")

# Normalizar campo activo
df["activo"] = (
    df["activo"]
    .astype(str)
    .str.strip()
    .str.lower()
)

verdaderos = df["activo"].isin(['true', '1', 'si', 'yes']).sum()

print(f"Existen {verdaderos} registros con 'activo' como verdadero.")