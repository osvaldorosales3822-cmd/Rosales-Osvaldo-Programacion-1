#EJERCICIO 1

ASKAGE = int(input("Introduce tu edad: "))
if ASKAGE <= 13: 
    print ("Nino")
elif ASKAGE <= 17:
    print ("adolescente")
else:
    print ("adulto")

#EJERCICIO 2

Usuario_Correcto = "NOUT"
Contrasena_Correcta = "64"


Usuario = input("Introduce tu usuario: ")
Contrasena = input("Introduce tu contrasena: ")

if (Usuario == Usuario_Correcto and Contrasena == Contrasena_Correcta):
    print ("Datos correctos")
elif (Usuario == "" and Contrasena == ""):
    print ("Error ")
else:
    print ("Datos incorrectos")

#3

PESO = int(input("introduce el peso de tu producto:  "))

if PESO <= 1: 
    costo = 50
elif PESO  <= 5:
    costo = 90
else:
    costo = 150

if PESO > 10:
    costo = costo * 0.90

print ("El costo de envio es de: ", costo)

#Ejercicio 4 clasificar temperaturas 

Temperatura = int(input("Introduce la temperatura: "))

if Temperatura < 10:
    print ("Frio")
elif Temperatura <= 24:
    print ("Templado")
else:
    print ("Calor")

#Ejercicio 5 Calificacion con letras 

Cali = int(input("Introduce la calificacion: "))

if Cali >= 90: 
    print ("Su calificacion es A")
elif Cali >= 80 or Cali >= 89:
    print ("Su calificacion es B")
elif Cali >= 70 or Cali >= 79:
    print ("Su calificacion es C")
elif Cali >= 60 or Cali >= 69:
    print ("Su calificacion es D")
else:
    print ("Su calificacion es F")

#Ejercicio 6 Descuento por monto de compra 

compra = float(input("Introduce el monto de tu compra: $"))

if compra > 500:
    descuento = 0.20
elif compra > 200:
    descuento = 0.10
else: 
    descuento = 0

Montocdes = compra * descuento 
Total = compra - Montocdes

print ("Descuento aplicado:", descuento * 100, "%")
print ("Monto final a pagar: $", Total)

#Ejercicio 7 validar un rango con comparacion encadenada 

num = float(input("Introduce un numero: "))
if 1 <= num <= 100:
    print ("El numero esta en el rango")
else:
    print ("El numero no esta en el rango")

#Ejercicio 8 Clasificar el IMC 

peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))

imc = peso / estatura ** 2 

print ("Tu IMC es: ", imc)

if imc < 18.5:
    print ("Clasificacion: Bajo peso")
elif imc < 25:
    print ("Clasificacion: Peso normal")
elif imc < 30:
    print ("Clasificacion: Sobrepeso")
else:
    print ("Obesidad")

#Ejercicio 9 Tarifas de electricidad 

consumo = float(input("Introduce el consumo mensual de electricidad en Kwh: "))

if consumo <= 150:
    costo1 = consumo * 1.20
elif consumo <= 300:
    costo1 = (150 * 1.20) + ((consumo - 150) * 1.80)  
else: 
    costo1 = (150 * 1.20) + (150 * 1.80) + ((consumo - 300) * 2.50)

print ("Consumo Total: ", consumo, "Kwh")
print ("Costo Total: $", costo1)


