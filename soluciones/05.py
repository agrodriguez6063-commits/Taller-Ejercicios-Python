import pandas as pd
import codecs

datos = pd.read_csv('data/personas.csv')

datos['apellido'] = datos['apellido_cifrado'].apply(lambda x: codecs.encode(x,'rot13').split()[-1])

frecuencias = datos['apellido'].value_counts()

print("El apellido más frecuente es:", frecuencias.idxmax())
print("Aparece:", frecuencias.max(), "veces")