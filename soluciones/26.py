import pandas as pd
import re

df = pd.read_csv("data/personas.csv", dtype=str)

# ---- limpiar ciudad ----
df["ciudad"] = (
    df["ciudad"]
    .str.lower()
    .str.replace(r"[^a-záéíóúñ\s]", "", regex=True)
    .str.strip()
)

# ---- limpiar activo ----
def limpiar_activo(x):
    x = re.sub(r"[^a-zA-Z0-9]", "", str(x)).lower()
    if x in ["true", "1", "yes", "si"]:
        return True
    if x in ["false", "0", "no"]:
        return False
    return None

df["activo"] = df["activo"].apply(limpiar_activo)

# ---- limpiar fecha ----
df["fecha_nacimiento"] = (
    df["fecha_nacimiento"]
    .str.replace(r"[^0-9\-/.]", "", regex=True)
    .str.replace(r"[/.]", "-", regex=True)
)

df["fecha_nacimiento"] = pd.to_datetime(df["fecha_nacimiento"], errors="coerce")

# ---- filtro final ----
resultado = df[
    (df["ciudad"] == "barranquilla") &
    (df["activo"] == True) &
    (df["fecha_nacimiento"].dt.year > 1980)
]

print(len(resultado))