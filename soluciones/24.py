import pandas as pd
import unicodedata
import codecs

df = pd.read_csv("data/personas.csv")

def quitar_tildes(texto):
    return unicodedata.normalize('NFD', str(texto)).encode('ascii', 'ignore').decode('utf-8')

# Descifrar nombres ROT13
df["nombre"] = df["nombre_cifrado"].apply(lambda x: codecs.decode(str(x), 'rot_13'))

# Limpiar nombre
df["nombre"] = (
    df["nombre"]
    .apply(quitar_tildes)
    .str.replace(r"[^a-zA-Z ]", "", regex=True)
    .str.strip()
    .str.lower()
)

# Limpiar profesion
df["profesion"] = (
    df["profesion"]
    .apply(quitar_tildes)
    .str.replace(r"[^a-zA-Z ]", "", regex=True)
    .str.strip()
    .str.lower()
)

# Filtrar Ana que sean Medico
cantidad = df[(df["nombre"] == "ana") & (df["profesion"] == "medico")].shape[0]

print(f"Registros con nombre 'Ana' que son 'Medico': {cantidad}")