# abriendo el archivo con with open
with open("text.txt", encoding="UTF-8") as archivo:
    # leemos el archivo
    contenido = archivo.read()
    # mostramos el resultado
    print(contenido)
    
# no es necesario cerrarlo al usar with open