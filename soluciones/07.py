import pandas as pd

df = pd.read_csv('data/personas.csv')

df["ciudad"] = (
    df["ciudad"]
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace("í","i")
    .str.replace(r"[@*!%#_]", "", regex=True)
)

# contar registros de Bogota
cantidad = (df['ciudad'] == 'medellin').sum()

print("Registros con ciudad Medellin:", cantidad)