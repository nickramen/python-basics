# Creando un conjunto con set()
conjunto = set(["Dato1","Dato2"])

# Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}

print(conjunto2)

# Los sets no se modifican
# Superconjuntos
# Subconjuntos


#Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}
conjunto3 = {2,4,6,8}

# verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

# verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 >   conjunto1

# Verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto3)

print(resultado)