import pandas as pd
import unicodedata
import re

# 1. Cargar datos
RUTA_ARCHIVO='data/personas.csv'
datos = pd.read_csv(RUTA_ARCHIVO)  

# 2. Función de limpieza
def limpiar_nombre(nombre):
    if pd.isna(nombre):
        return None
    
    # Convertir a string y quitar espacios al inicio/final
    nombre = str(nombre).strip()
    
    # Convertir a minúsculas
    nombre = nombre.lower()
    
    # Eliminar tildes y caracteres especiales
    nombre = unicodedata.normalize('NFKD', nombre)
    nombre = nombre.encode('ascii', 'ignore').decode('utf-8')
    
    # Eliminar números
    nombre = re.sub(r'\d+', '', nombre)
    
    # Eliminar caracteres especiales (solo letras y espacios)
    nombre = re.sub(r'[^a-z\s]', '', nombre)
    
    # Eliminar espacios múltiples
    nombre = re.sub(r'\s+', ' ', nombre).strip()
    
    return nombre if nombre else None

# 3. Aplicar limpieza a la columna de nombres
datos['nombre_limpio'] = datos['nombre'].apply(limpiar_nombre)

# 4. Eliminar valores nulos
datos_limpio = datos.dropna(subset=['nombre_limpio'])

# 5. Encontrar el nombre más frecuente
nombre_frecuente = datos_limpio['nombre_limpio'].value_counts()
nombre_top = nombre_frecuente.index[0]
cantidad_top = nombre_frecuente.iloc[0]

print(f"Nombre más frecuente: {nombre_top.title()}")
print(f"Veces que aparece: {cantidad_top}")