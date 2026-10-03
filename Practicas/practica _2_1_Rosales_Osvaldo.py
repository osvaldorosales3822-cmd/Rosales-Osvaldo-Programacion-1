#Ejercicio 1 Datos personales

Nombre = "Osvaldo"
Edad = "20"
Ciudad = "Tlaquepaque"

print (Nombre,Edad,Ciudad)

#Ejercicio 2 Actualizar un contador

Contador = 0
Contador = Contador + 1
print (Contador) 

contador = Contador + 1 
print (contador)

contador = contador + 1
print (contador)

#Ejercicio 3 Constante de conversion

PULGADA = 2.54
PULGADA_USUARIO = float (input ("Ingrese la cantidad de pulgadas a convertir: "))
CENTIMETROS = PULGADA_USUARIO * PULGADA
print (CENTIMETROS)

#Ejercicio 4 Area de un rectangulo

Base = 35 
Altura = 12
Area = Base * Altura 
print ("El area del rectangulo es: ", Area)

#Ejercicio 5 Total con IVA 

IVA = 0.16
Precio = 550 
Total_IVA1 = Precio + (Precio * IVA)
print ("Total es:",Total_IVA1)

Precio = 364
Total_IVA2 = Precio + (Precio * IVA)
print ("Total es:",Total_IVA2)

#Ejercicio 6 Intercambio de valores

Variable_A = 35 
Variable_B = 30

print ("antes", Variable_A, Variable_B)

Variable_A, Variable_B = Variable_B, Variable_A

print ("despues", Variable_A, Variable_B)

#Ejercicio 7 Identificar con type 

Edad = 20
Altura = 1.75
Nombre = "Osvaldo"
Vivo = True

print (type(Edad))
print (type(Altura))
print (type(Nombre))
print (type(Vivo))

#Ejercicio 8 Convertit tipos

TextoNum = "30"
Numero = int(TextoNum)
print (Numero)

NumeroTex = 20
Texto = str(NumeroTex)
print (Texto)

#Ejercicio 9 Booleanos y comparaciones 

X = 15
Y = 5

Mayor = X > Y 
# x = 5, y = 15 → Mayor = True
print (type(Mayor),Mayor)
