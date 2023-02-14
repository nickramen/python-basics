with open("newtext.txt","w",encoding="UTF-8") as archivo:
    # Sobreescribiendo el archivo
    #archivo.write("Jajajajaj")
    
    # agregando 2 lineas con writelines
    archivo.writelines(["Hola de nuevo\n","Este es un nuevo texto\n"])
    # agregando otras dos lineas
    archivo.writelines(["Hola de nuevo a vos Nicole\n","Este es un nuevo texto que escribi para vos\n"])