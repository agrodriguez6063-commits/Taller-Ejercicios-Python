import pandas as pd
import unicodedata

df = pd.read_csv('data/personas.csv')

def quitar_tildes(texto):
    return unicodedata.normalize('NFD', str(texto)).encode('ascii', 'ignore').decode('utf-8')

# Limpiar profesión
df["profesion"] = (
    df["profesion"]
    .apply(quitar_tildes)
    .str.replace(r'\t', '', regex=True)
    .str.replace(r'\d+', '', regex=True)   # eliminar números
    .str.strip()
    .str.lower()
    .str.replace(r"[@*!%#_]", "", regex=True)
    .str.replace(r"[^a-zA-Z ]", "", regex=True)
)

# Contar ingenieros
cantidad = (df["profesion"] == "ingeniero").sum()

print("Registros con profesión Ingeniero:", cantidad)