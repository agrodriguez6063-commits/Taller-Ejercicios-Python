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

correcciones = {
    'abogdo': 'abogado', 'administrdor': 'administrador',
    'arquitcto': 'arquitecto', 'chf': 'chef', 'contdor': 'contador',
    'crpintro': 'carpintero', 'disndor': 'disenador', 'economist': 'economista',
    'elctricist': 'electricista', 'enfrmro': 'enfermero', 'ingniro': 'ingeniero',
    'mcnico': 'mecanico', 'mdico': 'medico', 'plomro': 'plomero',
    'priodist': 'periodista', 'profsor': 'profesor', 'progrmdor': 'programador',
    'trductor': 'traductor', 'vtrinrio': 'veterinario',
}
df["profesion"] = df["profesion"].replace(correcciones)

# Limpiar salario
def limpiar_salario(valor):
    texto = str(valor).strip()
    texto = texto.replace('l', '1').replace('O', '0')
    texto = texto.replace(',', '.')
    numeros = re.findall(r'\d+\.?\d*', texto)
    return numeros[0] if numeros else None

df["salario"] = df["salario"].apply(limpiar_salario)
df["salario"] = pd.to_numeric(df["salario"], errors='coerce')

# Profesion con salario promedio más alto
resultado = (
    df.groupby("profesion")["salario"]
    .mean()
    .idxmax()
)

promedio = df.groupby("profesion")["salario"].mean().max()

print(f"La profesión con salario promedio más alto es '{resultado}' con {promedio:,.2f}")