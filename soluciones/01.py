import pandas as pd
datos = pd.read_csv('data/personas.csv')

# Cuenta filas donde 'id' tiene caracteres NO numéricos
cantidad = datos[~datos['id'].astype(str).str.match(r'^\d+$')].shape[0]

print(f"Filas con id no numérico: {cantidad}")