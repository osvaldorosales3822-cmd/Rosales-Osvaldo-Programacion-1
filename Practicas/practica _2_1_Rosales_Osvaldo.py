#Ejercicio 1 Datos personales

Nombre = "Osvaldo"
Edad = "20"
Ciudad = "Tlaquepaque"

Nombre2 = "Diego"
Edad2 = "18"
Ciudad2 = "Guadalajara"


print (Nombre,Edad,Ciudad)
print (Nombre2,Edad2,Ciudad2)

#Ejercicio 2 Actualizar un contador

Contador = 0
Contador = Contador + 1
print ("Contador:",Contador) 

contador = Contador + 1 
print ("Contador:",contador)

contador = contador + 1
print ("Contador:",contador)

#Ejercicio 3 Constante de conversion

PULGADA_A_CM = 2.54
CENTIMETRO_USUARIO = 90
CENTIMETROS = CENTIMETRO_USUARIO * PULGADA_A_CM
print ("CENTIMETROS:",CENTIMETROS) 

PULGADA = 2.54
CENTIMETRO_USUARIO = 85
CENTIMETROS = CENTIMETRO_USUARIO * PULGADA_A_CM
print ("CENTIMETROS:",CENTIMETROS)

#Ejercicio 4 Area de un rectangulo

Base = 35 
Altura = 12
Area = Base * Altura 
print ("El area del rectangulo es: ", Area)

Base = 20
Altura = 15 
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

Variable_C = 15
Variable_D = 40

print ("antes", Variable_C, Variable_D)

Variable_C, Variable_D = Variable_D, Variable_C

#Ejercicio 7 Identificar con type 

Edad = 20
Altura = 1.75
Nombre = "Osvaldo"
Vivo = True

print (type(Edad),type(Altura),type(Nombre),type(Vivo))

Edad1 = 19 
Altura1 = 1,70 
Nombre1 = "Yamir"
Vivo1 = True

print (type(Edad1),type(Altura1),type(Nombre1),type(Vivo1))


#Ejercicio 8 Convertit tipos

TextoNum = "30"
Numero = int(TextoNum)
print (Numero)

NumeroTex = 20
Texto = str(NumeroTex)
print (Texto)

TextoNum2 = "300"
Numero2 = int(TextoNum)
print (Numero)

NumeroTex = 400
Texto = str(NumeroTex)
print (Texto)



#Ejercicio 9 Booleanos y comparaciones 

X = 15
Y = 5

Mayor = X > Y 
# x = 5, y = 15 → Mayor = True
print (type(Mayor),Mayor)

X2 = 78
Y2 = 40

Mayor = X2 > Y2 
# x = 5, y = 15 → Mayor = True
print (type(Mayor),Mayor)

