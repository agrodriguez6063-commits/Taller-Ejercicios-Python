import pandas as pd

df = pd.read_csv("data/personas.csv")

# Convertir a fecha
df["fecha_nacimiento"] = pd.to_datetime(df["fecha_nacimiento"], errors="coerce")

# Definir fecha actual del ejercicio
fecha_actual = pd.Timestamp("2026-02-26")

# Calcular edad
edad = (fecha_actual - df["fecha_nacimiento"]).dt.days // 365

# Contar personas con más de 50 años
cantidad = (edad > 50).sum()

print(f"{cantidad} personas tienen más de 50 años.")