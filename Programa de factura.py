print("Bienvenido a CANTECH")
productos = []
valor_productos = []
cantidad_productos = []
cantidad = int(input("¿Cuantos modelos de camaras deseas comprar?  ---> "))
i=0
suma=0
while i<cantidad:
    producto = input("Ingrese el modelo de la camara (XSecurity, Risco, Paradox) ---> ")
    valor_producto = int(input("Valor por unidad de la camara (XSecurity 250, Risco 300, Paradox 325) ---> "))
    cantidad_producto = int(input("¿Cuantas cantidades de "+producto+" quieres comprar?  ---> "))
    productos.append(producto)
    valor_productos.append(valor_producto)
    cantidad_productos.append(cantidad_producto)
    total = cantidad_producto*valor_producto
    suma = total+suma
    i+=1
print(suma)

if suma <500:
    print("No aplica para el descuento, el total de su producto es de --->" ,suma)
elif suma >= 500 and suma <1500:
    print("Gracias por su compra, se le aplico un descuento del 10%")
    division = suma*(10/100)
    descuento = suma-division
    print("Ahora tendra que pagar una cantidad de",descuento)

elif suma >=1500:
    print("Gracias por su compra, se le aplico un descuento del 15%")
    division = suma*(15/100)
    descuento = suma-division
    print("Ahora tendra que pagar una cantidad de",descuento)
print("\n***Factura***")
print("\nNombres de productos ----> ",productos," \nPrecios originales de productos ----> ",valor_productos, " \nCantidad de Productos ----> ",cantidad_productos)