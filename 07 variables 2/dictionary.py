# Creando diccionarios con dict()
diccionario = dict(nombre="Nicole",apellido="Ramos")

#Las listas no puede ser claves y usamos frozensets para meter conjuntos
diccionario = {frozenset(["Nicole","Ramos"]): "jajaja"}

# Creando diccionarios con fromkeys() y por defecto: nonce
diccionario = dict.fromkeys(["nombre","apellido"])

# Creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"], "No se")

print(diccionario)