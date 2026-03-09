import pandas as pd
import unicodedata
import codecs
import re

df = pd.read_csv("data/personas.csv")

def quitar_tildes(texto):
    return unicodedata.normalize('NFD', str(texto)).encode('ascii', 'ignore').decode('utf-8')

# ---- descifrar nombre y apellido ROT13 ----
df["nombre"] = df["nombre_cifrado"].apply(lambda x: codecs.decode(str(x), 'rot_13'))
df["apellido"] = df["apellido_cifrado"].apply(lambda x: codecs.decode(str(x), 'rot_13'))

# ---- limpiar nombre ----
df["nombre"] = (
    df["nombre"]
    .apply(quitar_tildes)
    .str.replace(r"[^a-zA-Z ]", "", regex=True)
    .str.strip()
    .str.lower()
)

# ---- limpiar apellido ----
df["apellido"] = (
    df["apellido"]
    .apply(quitar_tildes)
    .str.replace(r"[^a-zA-Z ]", "", regex=True)
    .str.strip()
    .str.lower()
)

# ---- limpiar email ----
df["email"] = (
    df["email"]
    .str.strip()
    .str.lower()
    .str.replace(r"\s+", "", regex=True)
    .str.replace(r"[^\w@.\-]", "", regex=True)
)

# ---- filtrar dominio gmail.com ----
resultado = df[
    df["email"].str.endswith("@gmail.com", na=False)
]

print(len(resultado))