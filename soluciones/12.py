import pandas as pd

df = pd.read_csv("data/personas.csv")

# Contar registros donde el email tiene espacios al inicio, al final o en medio
cantidad = df["email"].apply(lambda x: str(x) != str(x).strip() or ' ' in str(x).strip()).sum()

print(f"Existen {cantidad} registros con espacios adicionales en el campo email.")