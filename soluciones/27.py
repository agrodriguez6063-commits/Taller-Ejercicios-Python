import pandas as pd
import unicodedata
import codecs

df = pd.read_csv("data/personas.csv")

# --- Función de limpieza ---
def quitar_tildes(texto):
    return unicodedata.normalize('NFD', str(texto)).encode('ascii', 'ignore').decode('utf-8')

def normalizar_texto(texto):
    return quitar_tildes(str(texto)).strip().lower()

# --- Limpieza de columnas ---
df["profesion_limpia"] = df["profesion"].apply(normalizar_texto)
df["ciudad_limpia"] = df["ciudad"].apply(normalizar_texto)

# --- Filtrar ingenieros y contar por ciudad ---
ingenieros = df[df["profesion_limpia"] == "ingeniero"]

ciudad_top = ingenieros["ciudad_limpia"].value_counts().idxmax()
cantidad = ingenieros["ciudad_limpia"].value_counts().max()

print(f"Ciudad con más ingenieros: {ciudad_top.title()} ({cantidad} ingenieros)")