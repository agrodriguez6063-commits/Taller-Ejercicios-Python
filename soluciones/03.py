# cargar datos
import pandas as pd
import codecs
datos = pd.read_csv('data/personas.csv')
texto_original = "Juan"

#resolver ejercicio
#Cifrar (ROT13)
texto_cifrado = codecs.encode(texto_original, 'rot_13')
print(f"Cifrado: {texto_cifrado}")

#Maria = Znevn

condicion = datos['nombre_cifrado']=='Whna'
datos_nuevos = datos[condicion]
print( "El número de repeticiones de Juan es: ", datos_nuevos.shape[0])