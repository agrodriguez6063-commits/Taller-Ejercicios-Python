import pandas as pd
import unicodedata
import codecs

df = pd.read_csv("data/personas.csv")

def quitar_tildes(texto):
    return unicodedata.normalize('NFD', str(texto)).encode('ascii', 'ignore').decode('utf-8')

# Descifrar nombres y apellidos ROT13
df["nombre"] = df["nombre_cifrado"].apply(lambda x: codecs.decode(str(x), 'rot_13'))
df["apellido"] = df["apellido_cifrado"].apply(lambda x: codecs.decode(str(x), 'rot_13'))

# Limpiar nombre
df["nombre"] = (
    df["nombre"]
    .apply(quitar_tildes)
    .str.replace(r"[^a-zA-Z ]", "", regex=True)
    .str.strip()
    .str.lower()
)

# Limpiar apellido
df["apellido"] = (
    df["apellido"]
    .apply(quitar_tildes)
    .str.replace(r"[^a-zA-Z ]", "", regex=True)
    .str.strip()
    .str.lower()
)

cantidad = df[
    (df["nombre"] == "jose") &
    (df["apellido"] == "garcia")
].shape[0]

print(f"Registros con nombre 'Jose' y apellido 'Garcia': {cantidad}")