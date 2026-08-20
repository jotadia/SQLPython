# -*- coding: utf-8 -*-
"""
Created on 19 aug 2026

@author: JCOD
"""
import datetime
#import MyCRUD

from crud import MyCRUD

crud = MyCRUD()

"""try:
    crud.crear_tabla()
    print("Tablas creadas exitosamente.")

except Exception as e:
    print(f"Error al crear las tablas: {e}")
    

try:
    crud.insertar_cliente("Juan Perez", "juan.perez@example.com")
    crud.insertar_cliente("Rodriguez", "rodri.guez@example.com")
    crud.insertar_cliente("Maria", "maria@example.com")
    print("Clientes insertados exitosamente.")
except Exception as e:
    print(f"Error al insertar el cliente: {e}")

try:
    crud.insertar_producto("Laptop", 1500.00, 10)
    crud.insertar_producto("Cebolla", 20.00, 10)
    crud.insertar_producto("Arroz", 5.00, 20)
    print("Productos insertados exitosamente.")
except Exception as e:
    print(f"Error al insertar el producto: {e}")
    """
    


opcion = input("Selecciona una opción: \n1. Crear un Cliente.\n2. Crear un Producto.\n3. Ver los clientes.\n4. Ver los productos.\n5. Ver las ventas.\n6. Comprar un producto.\n7. Eliminar una venta.\n8. Salir.\n")

while opcion != "8":
    
    if opcion == "1":
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        correo_cliente = input("Ingrese el correo del cliente: ")   
        try:
            crud.insertar_cliente(nombre_cliente, correo_cliente)
        except Exception as e:
            print(f"Error al insertar el cliente: {e}") 
    elif opcion == "2": 
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = float(input("Ingrese el precio del producto: "))
        stock_producto = int(input("Ingrese el stock del producto: "))
        try:
            crud.insertar_producto(nombre_producto, precio_producto, stock_producto)
        except Exception as e:
            print(f"Error al insertar el producto: {e}")
    elif opcion == "3":
        try:
            clientes = crud.obtener_clientes()
            print("Clientes:")
            for cliente in clientes:
                print(f"ID: {cliente[0]}, Nombre: {cliente[1]}, Correo: {cliente[2]}")
        except Exception as e:
            print(f"Error al obtener los clientes: {e}")
    elif opcion == "4":
        try:
            productos = crud.obtener_productos()
            print("Productos:")
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Stock: {producto[3]}")
        except Exception as e:
            print(f"Error al obtener los productos: {e}")  
    elif opcion == "5":
        try:
            ventas = crud.consultar_ventas()
            print("Ventas:")
            for venta in ventas:
                print(f"ID: {venta[0]}, Cliente ID: {venta[1]}, Producto ID: {venta[2]}, Cantidad: {venta[3]}, Fecha de Venta: {venta[4]}")
        except Exception as e:
            print(f"Error al obtener las ventas: {e}")
    elif opcion == "6":
        cliente_id = int(input("Ingrese el ID del cliente: "))
        producto_id = int(input("Ingrese el ID del producto: "))
        cantidad = int(input("Ingrese la cantidad a comprar: "))
        try:
            crud.insertar_venta(cliente_id, producto_id, cantidad, datetime.date.today())
        except Exception as e:
            print(f"Error al realizar la compra: {e}")  
    elif opcion == "7":
        venta_id = int(input("Ingrese el ID de la venta a eliminar: "))
        try:
            crud.eliminar_venta(venta_id)
        except Exception as e:
            print(f"Error al eliminar la venta: {e}")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.\n1. Crear un Cliente.\n2. Crear un Producto.\n3. Ver los clientes.\n4. Ver los productos.\n5. Ver las ventas.\n6. Comprar un producto.\n7. Eliminar una venta.\n8. Salir.\n")
    
    opcion = input("Selecciona una opción: \n1. Crear un Cliente.\n2. Crear un Producto.\n3. Ver los clientes.\n4. Ver los productos.\n5. Ver las ventas.\n6. Comprar un producto.\n7. Eliminar una venta.\n8. Salir.\n")