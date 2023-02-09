# conjuntos
animales = ("gato","perro","loro","cocodrilo")
numeros = (10,54,14,53)

# Recorriendo conjunto animales

for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')
    
    
# Recorriendo el conjunto numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
    
for numero, animal in zip(animales, numeros):
    print(f'recorriendo conjunto 1: {numero}')
    print(f'recorriendo conjunto 2: {animal}')
    

for num in range(5,10):
    print(num)
    
# Forma no optima de recorrer un conjunto
for num in range(len(numeros)):
    print(numeros[num])
    
# Forma correcta de recorrer un conjunto con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es: {indice} y el valor es: {valor}')
    

# Usando el for/else
for numero in numeros:
    print(f'Ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print(f'el bucle termino')
    
    
