###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
print("Daniel Hernandez","Izcalli, Estado de Mexico", sep="\n",end="\n")


print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print("a: ",type(a))
print("b: ",type(b))
print("c: ",type(c))
print("d: ",type(d))
print("e: ",type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")


### Completa aquí
num_1 = "12345"
print("num_1 =",type(num_1))
num_1 = int(num_1)
print("num_1 =",type(num_1))
num_1 = float(num_1)
print("num_1 =",type(num_1))

num_2 = 3.99
print("num_2 =",type(num_2))
num_2 = int(num_2)
print("num_2 =",type(num_2),"el float fue redondeado a 4")

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
my_name = "Daniel"
my_age = 25
my_height = 1.75

print(f"Buenas! Mi nombre es {my_name}, tengo {my_age}, mido {my_height} metros")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

print("Resultado =",int(round(3.1416)/2))