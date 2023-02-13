#importando un modulo y asignadole el nombre "m_saludar"
#import module_greeting.py as m_saludar

#desde ese modulo, importamos dos funciones y les cambiamos el nombre
from module_greeting import saludar as saludar_normal, saludar_raro as saludar_bien_raro

#creamos las variables
saludo = saludar_normal("Nicole")
saludo_raro = saludar_bien_raro("Darcy")

#mostramos los resultado
print(saludo)
print(saludo_raro)