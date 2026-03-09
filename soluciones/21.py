import pandas as pd

df = pd.read_csv("data/personas.csv")

# Convertir la columna a formato fecha
df["fecha_nacimiento"] = pd.to_datetime(df["fecha_nacimiento"], errors="coerce")

# Contar personas nacidas antes de 1960
cantidad = (df["fecha_nacimiento"].dt.year < 1960).sum()

print(f"{cantidad} personas nacieron antes de 1960.")