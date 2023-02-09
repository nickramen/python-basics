diccionario = {
    "nombre": "Lucas",
    "apellido": "Dalto",
    "subs": 1000000
}

# Recorriendo diccionario con items() para obtener las claves
for key in diccionario.items():
    key
    print(f'La clave es: {key}')

# Recorriendo diccionario con items() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'La clave es: {key} y el valor es: {value}')