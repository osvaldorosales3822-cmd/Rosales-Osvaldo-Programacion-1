# Nombre: Osvaldo Yahir Rosales Tello
# Codigo de estudiante: 223038226

# ==========================================
# 1. DEFINICION DE CLASES Y CONFIGURACION
# ==========================================

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre 
        self.precio = precio
        self.cantidad = cantidad

# Catalogo oficial de la papeleria (Codigo: {Nombre, Precio})
CATALOGO = {
    "4500": {"nombre": "Pintura Oleo", "precio": 120.00},
    "4400": {"nombre": "Pintura Acrilica", "precio": 85.00},
    "4300": {"nombre": "Lienzo Chico", "precio": 60.00},
    "4200": {"nombre": "Lienzo Mediano", "precio": 95.00},
    "4100": {"nombre": "Lienzo Grande", "precio": 150.00},
    "3300": {"nombre": "Cuaderno Raya", "precio": 45.00},
    "3200": {"nombre": "Cuaderno Cuadro", "precio": 45.00},
    "3100": {"nombre": "Cuaderno Blanco", "precio": 50.00},
    "2200": {"nombre": "Lapiz 2B", "precio": 12.00},
    "2100": {"nombre": "Pluma NRA", "precio": 15.00},
    "1200": {"nombre": "Hojas Blancas (Paquete)", "precio": 85.00},
    "1100": {"nombre": "Hojas Color (Paquete)", "precio": 95.00}
}

# Lista global para almacenar el carrito de compras
productos_comprados = []

# ==========================================
# 2. BIENVENIDA Y CAPTURA INICIAL
# ==========================================

print("==================================================")
print(" Bienvenido al sistema de ventas Papeleria El Sol ")
print("==================================================\n")

# Solicitar cuantos artículos se van a procesar en total
c_input = input("¿Cuantos productos diferentes va a registrar? ")

# Validar que la respuesta sea un numero entero positivo
while not c_input.isdigit() or int(c_input) <= 0:
    print(" ERROR: Debe ingresar un número entero mayor a 0.")
    c_input = input("¿Cuántos productos diferentes va a registrar? ")

cantidad_productos = int(c_input)

# ==========================================
# 3. PROCESAMIENTO Y VALIDACION DE PRODUCTOS
# ==========================================

for i in range(cantidad_productos):
    print(f"\n--- Producto {i + 1} de {cantidad_productos} ---")
    
    # Inicializacion de variables de control
    codigo_valido = False
    nombre_producto = ""
    precio_producto = 0.0
    
    # Bucle para validar el codigo numérico del catálogo
    while not codigo_valido:
        codigo = input("Ingrese el codigo numerico del producto: ").strip()
        if codigo in CATALOGO:
            nombre_producto = CATALOGO[codigo]["nombre"]
            precio_producto = CATALOGO[codigo]["precio"]
            print(f"-> Seleccionado: {nombre_producto} (${precio_producto:.2f})")
            codigo_valido = True
        else:
            print(" Codigo no encontrado. Intente de nuevo (ej. 4500, 3300, 1100).")
            
    # Bucle para validar la cantidad de unidades solicitadas
    cantidad_input = input(f"Ingrese la cantidad de {nombre_producto}: ")
    while not cantidad_input.isdigit() or int(cantidad_input) <= 0:
        print(" ERROR: La cantidad debe ser un número entero mayor a 0.")
        cantidad_input = input(f"Ingrese la cantidad de {nombre_producto}: ")
        
    cantidad_producto = int(cantidad_input)
    
    # Crear la instancia del objeto Producto y anadirlo a la lista de compras
    nuevo_producto = Producto(nombre_producto, precio_producto, cantidad_producto)
    productos_comprados.append(nuevo_producto)

# ==========================================
# 4. CALCULOS FINALES Y EMISION DE RECIBO
# ==========================================

subtotal_general = 0.0

print("\n==================================================")
print("                 RECIBO DE COMPRA                 ")
print("==================================================")
print(f"{'Producto':<25} {'Cant.':<6} {'Precio':<9} {'Subtotal':<9}")
print("--------------------------------------------------")

# Listado dinamico de los artículos adquiridos
for prod in productos_comprados:
    subtotal_producto = prod.precio * prod.cantidad
    subtotal_general += subtotal_producto
    
    # Formateo de columnas alineadas con montos a 2 decimales
    print(f"{prod.nombre:<25} {prod.cantidad:<6} ${prod.precio:<8.2f} ${subtotal_producto:<8.2f}")

print("--------------------------------------------------")

# Calculo de impuestos vigentes (IVA 16%)
iva = subtotal_general * 0.16
total_pagar = subtotal_general + iva

# Desglose financiero final
print(f"{'Subtotal General:':<33} ${subtotal_general:>8.2f}")
print(f"{'IVA (16%):':<33} ${iva:>8.2f}")
print("==================================================")
print(f"{'TOTAL A PAGAR:':<33} ${total_pagar:>8.2f}")
print("==================================================\n")
print("¡Gracias por su compra en Papeleria El Sol!")
