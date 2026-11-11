
#EJERCICIOS DE CLASE

matriz = [
    [1,2,3],
    [4,5,6]
]

print (matriz [0][0])
print (matriz [0][1])
print (matriz [0][2])
print (matriz [1][1])


matriz = [
    ["S","O","R","R"],
    ["R","E","S"]
]

print (matriz [0][2])
print (matriz [1][1])

frutas = ["manzana","pera"]
frutas.append("uva") #agrega al final
frutas.insert(1, "kiwi") #agrega en la posicion 1
frutas.insert(0, "cereza")

print(frutas)


frutas.remove("pera") #elimina por valor
frutas.pop(0) #elimina por indice
del     frutas[0] #elimina por indice
print(frutas)

clave = ""
while clave != "Nout64":
    clave = input("Contrasena : ")
print("Acceso permitido")

while True:
    print("Se ejecuta al menos una vez")
    user_input = input("Continuar? (y/n): ")
    if user_input.lower() != 'y': #upper()
        break


#for _ in range(5):
#    contador = contador + 1
#print (contador)

#NameError: contador
#NO existe


contador = 0 
for _ in range(5):
    contador = contador + 1
print (contador)

#Empieza en 0, luego suma

Precios = [50, 120, 30]
total = 0
for precio in Precios:
    total = total + precio 
print (total)

notas = [8,9,7,6]
notas.append(10)  #inserta al final
notas.remove(6)   #elimina la reprobatoria 
print(7 in notas) #busca si existe
print(notas)


salon = [
["Ana,", "Luis"],
["Eva","Ivan"]
]

print(salon)
print(salon[1][0]) #Fila 1, columno 0
salon[0][1] = "Carla" #Reemplaza un alumno
print(salon)

for fila in range(3):
    for columna in range(3):
        print("*", end="  ")
    print()

for fila in range(1,3):
    for columna in range(1,3):
        print(fila, columna)

for i in range(1,4):
    for j in range(1,4):
        resultado = i * j
        print(i,"x",j,"=",resultado)


