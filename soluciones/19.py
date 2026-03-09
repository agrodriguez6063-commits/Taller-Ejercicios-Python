import pandas as pd

df = pd.read_csv("data/personas.csv")

# Detectar fechas que NO cumplen el formato YYYY-MM-DD
incorrectas = ~df["fecha_nacimiento"].astype(str).str.match(r"^\d{4}-\d{2}-\d{2}$")

cantidad = incorrectas.sum()

print(f"Existen {cantidad} registros con formato de fecha diferente a YYYY-MM-DD.")