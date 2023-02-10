# creando una funcion de 3 parametros
# def frase(nombre,apellido,adjetivo):
#     return f'Hola, {nombre} {apellido}, sos muy {adjetivo}'

# utilizando keyword arguments
# frase_resultante = frase(adjetivo="capo", nombre="Lucas",apellido="Dalto")

# creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo="inteligente"):
    return f'Hola, {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase("Nicole","Ramos","masisa")

print(frase_resultante)