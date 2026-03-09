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

# Limpiar ciudad
df["ciudad"] = (
    df["ciudad"]
    .apply(quitar_tildes)
    .str.replace(r'\t', '', regex=True)
    .str.replace(r"[^a-zA-Z ]", "", regex=True)
    .str.strip()
    .str.lower()
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

cantidad = df[(df["nombre"] == "carlos") & (df["ciudad"] == "cali")].shape[0]

print(f"Registros con nombre 'Carlos' que viven en Cali: {cantidad}")