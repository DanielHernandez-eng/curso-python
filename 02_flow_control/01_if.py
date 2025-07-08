###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

import os
os.system("clear")

print("\n Sentencia simple condicional")

edad = 18
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

edad = 15
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

print("\n Sentencia condicional con else")
edad = 15
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")

print("\n Sentencia condicional con elif")
nota = 5

if nota >= 9:
  print("¡Sobresaliente!")
elif nota >= 7:
  print("Notable!")
elif nota >= 5:
  print("¡Aprobado!")
else:
  print("¡No está calificado!")

print("\n Condiciones múltiples")
edad = 16
tiene_carnet = True

# JavaScript
# && -> and
# || -> or

# 🇻🇪 un pueblo de Valencia
if edad >= 18 and tiene_carnet:
  print("Puedes conducir 🚗")
else:
  print("POLICÍA 🚔!!!!!!!")

# 🇻🇪 un pueblo de Isla Margarita
if edad >= 18 or tiene_carnet:
  print("Puedes conducir en la Isla Margarita 🚗")
else:
  print("Paga al policía y te deja conducir!!!")

es_fin_de_semana = False
# JavaScript -> !
if not es_fin_de_semana:
  print("¡midu, venga que hay que streamear!")


print("\n Anidar condicionales")
edad = 20
tiene_dinero = True

if edad >= 18:
  if tiene_dinero:
    print("Puedes ir a la discoteca")
  else:
    print("Quédate en casa")
else:
  print("No puedes entrar a la disco")

# Más fácil:
# if edad < 18:
#   print("No puedes entrar a la disco")
# elif tiene_dinero:
#   print("Puedes ir a la discoteca")
# else:
#   print("Quédate en casa")

numero = 5
if numero: # True
  print("El número no es cero")

numero = 0
if numero: # False
  print("Aquí no entrará nunca")

nombre = ""
if nombre:
  print("El nombre no es vacío")

numero = 3 # asignación
es_el_tres = numero == 3 # comparación

if es_el_tres:
  print("El número es 3")


print("\nLa condición ternaria:")
# es una forma concisa de un if-else en una línea de código
# [código si cumple la condición] if [condición] else [código si no cumple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
num_1,num_2 = input("Ingresa 2 numeros separados por un espacio").split()

if num_1 == num_2:
  print("los numeros son iguales")
elif num_1 > num_2:
  print(num_1, "Es el numero mayor")
elif num_2 > num_1:
  print(num_2, "Es el numero mayor")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

num_3,num_4 = input("Ingresa 2 numeros separados por un espacio").split()
num_3=int(num_3)
num_4=int(num_4)
operacion = input("¿Que operacion deseas realizar? (+, -, *, /)")

if operacion == "+":
  print("Resultado:",num_3 + num_4)
elif operacion == "-":
  print("Resultado:",num_3 - num_4)
elif operacion == "*":
  print("Resultado:",num_3 * num_4)
elif operacion == "/":
  if not num_4 == 0:
    print("Resultado:",num_3 - num_4)
  else:
    print("no se puede dividir entre zero")
else:
  print("La operación",operacion,"no existe")
  
# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
 
year = int(input("Ingresa un año:"))

if type(year/4) == "int" and type(year/100) ==  "float":
  print(year, "Es un año bisiesto")
elif type(year/400) == "int" and type(year/100) ==  "int":
  print(year, "Es un año bisiesto")
else:
  print (year, "No es un año bisiesto")


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("Introduce una edad:"))

if edad >= 0 and edad <=2:
  print("Bebé")
elif edad >= 3 and edad <=12:
  print("Niño")
elif edad >= 13 and edad <=17:
  print("Adolescente")
elif edad >= 18 and edad <=64:
  print("Adulto")
elif edad >= 65:
  print("Adulto Mayor")