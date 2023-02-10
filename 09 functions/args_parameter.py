# forma no optima de sumar valores
# def suma(lista):
#     numeros_sumados = 0
#     for numero in lista:
#         numeros_sumados = numeros_sumados + numero
#     return numeros_sumados
# resultado = suma([5,2,6,8,4,7])


#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([8,2,5,9,3,60])

print(resultado2)


# lo mismo pque arriba pero  utilizando el operador * como parametro  args()
def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma("Nicole",5,3,9,10,20,3)
