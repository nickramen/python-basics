frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "Hola Nicole"
numeros = [12,34,5,7]

# Evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'manzana ':
        continue
    print(f'Me voy a comer una {fruta}')
    

# Evitando que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == 'pera':
        break
else:
    print('Bucle terminado ')
    
# Recorrer una cadena de texto
for letra in cadena:
    print(letra)
    

# For en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)