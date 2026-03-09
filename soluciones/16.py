import pandas as pd
import re

df = pd.read_csv("data/personas.csv")

def limpiar_salario(valor):
    texto = str(valor).strip()
    texto = texto.replace('l', '1').replace('O', '0')
    texto = texto.replace(',', '.')
    numeros = re.findall(r'\d+\.?\d*', texto)
    return numeros[0] if numeros else None

df["salario"] = df["salario"].apply(limpiar_salario)
df["salario"] = pd.to_numeric(df["salario"], errors='coerce')

minimo = df["salario"].dropna().min()

print(f"El salario mínimo después de limpiar es: {minimo:,.2f}")