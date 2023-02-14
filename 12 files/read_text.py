# usnado open para abrir un archivo con una codificacion universal 
archivo = open("text.txt", encoding="UTF-8")

# leer archivo completo
#archivo = archivo.read()

# leer linea por linea
#lineas = archivo.readlines()

# leer una sola linea
linea = archivo.readline(100)

# cerrar el archivo
archivo.close
print(linea)