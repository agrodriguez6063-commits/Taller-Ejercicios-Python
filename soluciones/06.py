import pandas as pd

df = pd.read_csv('data/personas.csv')

df["ciudad"] = (
    df["ciudad"]
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace("á","a")
    .str.replace(r"[@*!%#_]", "", regex=True)
)

# contar registros de Bogota
cantidad = (df['ciudad'] == 'bogota').sum()

print("Registros con ciudad Bogota:", cantidad)