# creando una funcion simple
def saludar():
    print("Hey nicole, how's the #100DaysOfCode challenge going?")
    
    
saludar()

# crear una funcion que tenga parametros
def saludar1(nombre,sexo):
    sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "maestra"
    elif (sexo == "hombre"):
        adjetivo = "maestro"
    else:
        adjetivo = "amor"
    print(f'Hola {nombre}, mi {adjetivo}. Como estas?')

saludar1("Nicoooole","mujer")

# crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num -2
    c2 = num
    c3 = num -5
    password = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return password,num
    
# desempaquetndo la funcion
password,primer_numero = crear_contraseña_random(158)

# monstrando los resultados
print(f'Tu contraseña nueva es: {password}')
print(f'El numero utilizado para crearla fue: {primer_numero}')