import pandas as pd
import unicodedata
import re

df = pd.read_csv("data/personas.csv")

def quitar_tildes(texto):
    return unicodedata.normalize('NFD', str(texto)).encode('ascii', 'ignore').decode('utf-8')

# Limpiar profesion
df["profesion"] = (
    df["profesion"]
    .apply(quitar_tildes)
    .str.replace(r'\t', '', regex=True)
    .str.replace(r"[^a-zA-Z ]", "", regex=True)
    .str.strip()
    .str.lower()
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)


# Limpiar salario
def limpiar_salario(valor):
    texto = str(valor).strip()
    texto = texto.replace('l', '1').replace('O', '0')
    texto = texto.replace(',', '.')
    numeros = re.findall(r'\d+\.?\d*', texto)
    return numeros[0] if numeros else None

df["salario"] = df["salario"].apply(limpiar_salario)
df["salario"] = pd.to_numeric(df["salario"], errors='coerce')

cantidad = df[
    (df["profesion"] == "abogado") &
    (df["salario"] > 10000000)
].shape[0]

print(f"Registros con profesión 'Abogado' y salario > 10,000,000: {cantidad}")