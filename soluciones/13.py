import pandas as pd

df = pd.read_csv("data/personas.csv")

# Contar salarios que no son completamente numéricos
cantidad = (~df["salario"].astype(str).str.isnumeric()).sum()

print("Registros con caracteres no numéricos en salario:", cantidad)