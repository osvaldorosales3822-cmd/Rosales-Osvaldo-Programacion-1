
#ejercicio 1 par o impar 

Variable_Par = 30
Variable_Impar = 67

if Variable_Par % 2 == 0:
    print ("El numero es par")

if Variable_Impar% 2 != 0:
    print ("El numero es impar")

#ejercicio 2 sumas

Suma1 = "34" 
Suma2 = "40"

# sin Int
print (Suma1 + Suma2) 
# con Int
print (int(Suma1) + int(Suma2))

#Ejercicio 3 Mini reporte de un perfil

Nombre = "Diego Teles"
Edad = 18 
Estatura = 1.70
Es_Estudiante = False

print ((Nombre, Edad, Estatura, Es_Estudiante))
print (type(Nombre), type(Edad), type(Estatura), type(Es_Estudiante))


Nombre1 = "Sofia Amezcua" 
Edad1 = 21
Estatura1 = 1.60
Es_Estudiante1 = True

print ((Nombre1, Edad1, Estatura1, Es_Estudiante1))
print (type(Nombre1), type(Edad1), type(Estatura1), type(Es_Estudiante1))

mensaje_extra = "Hola el es " + Nombre + " y su edad es de " + str(Edad)
print (mensaje_extra)

mensaje_extra = "Hola ella es " + Nombre1 + " y su edad es de " + str(Edad1)
print (mensaje_extra)


#ejercicio 4 Operadores aritmeticos basicos

Numero1 = 9
Numero2 = 3 
print (str("A=")+ str(Numero1))
print (str("B=")+ str(Numero2))
print ("Suma:" , Numero1 + Numero2)
print ("Resta:" , Numero1 - Numero2)
print ("Multiplicacion:" , Numero1 * Numero2)
print ("Division" , Numero1 // Numero2)

A = 90
C = 30
print (str("A=")+ str(A))
print (str("C=")+ str(C))
print ("Division_Entera:" , A // C)
print ("Division_Residuo:" , A % C)

#división no exacta

B = 17
D = 5
print("B =", B)
print("D=", D)
print("División entera:", B // D)
print("Módulo o residuo:", B % D)

#Ejercicio 5 Operadores relacionales 

NumeroA = 10
NumeroB = 30

print ("Es mayor que?" , NumeroA > NumeroB)
print ("Es menor que?" , NumeroA < NumeroB)
print ("Es igual que?" , NumeroA == NumeroB)
print ("Es diferente que?" , NumeroA != NumeroB)

NumeroX = 64
NumeroY = 64

print ("Es mayor que?" , NumeroX > NumeroY)
print ("Es menor que?" , NumeroX < NumeroY)
print ("Es igual que?" , NumeroX == NumeroY)
print ("Es diferente que?" , NumeroX != NumeroY)

#Ejercicio 7 Operdadores Logicos 

VariableA = (40 > 10)
VariableB = (69 == 67)   

resultado_and = VariableA and VariableB
resultado_or = VariableA or VariableB
resultado_not = not VariableA

print("VariableA: (40 > 10):", VariableA)
print("VariableB: (69 == 67):", VariableB)
print("Combinación con AND:", resultado_and)
print("Combinación con OR:", resultado_or)
print("Combinación con NOT (invirtervencion a VariableA):", resultado_not)

#Ejercicio 8 Promedio y Aprobacion

calificacion1 = 7.8
calificacion2 = 7.7
calificacion3 = 8.0
promedio = (calificacion1 + calificacion2 + calificacion3) / 3
aprobado = (promedio >= 6)
print("Promedio obtenido: ",promedio)
print("¿Está aprobado?: ",aprobado) 

#Ejercicio 9 Validacion de elegibilidad

Edad = 20
Nacionalidad = "Mexicana"
Es_Elegible = (Edad > 17) and (Nacionalidad == "Mexicana")
print("¿Es elegible?:", Es_Elegible)
Es_elegible_or = (Edad > 17) or (Nacionalidad == "Mexicana")
print("Extra:", Es_elegible_or)

Edad = 13
Nacionalidad = "Peruana"
Es_Elegible = (Edad > 17) and (Nacionalidad == "Mexicana")
print("¿Es elegible?:", Es_Elegible)
print("Extra:", Es_elegible_or)

Edad = 16
Nacionalidad = "Chilena"
Es_Elegible = (Edad > 17) and (Nacionalidad == "Mexicana")
print("¿Es elegible?:", Es_Elegible)
print("Extra:", Es_elegible_or)




