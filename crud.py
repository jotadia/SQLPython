# -*- coding: utf-8 -*-
"""
Created on 19 aug 2026

@author: JCOD
"""

#import  MyDataBase

from database import MyDataBase


class MyCRUD:
    def __init__(self):
        self.db = MyDataBase()  
        
    def crear_conexion(self):
        return self.db.crear_conexion() 
    
    def crear_tabla(self):
        conexion = self.crear_conexion()
        cursor = conexion.cursor()
        
        #Tabla clientes
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100),
                correo VARCHAR(50)
            )
        """)
        conexion.commit()
        
        #Tabla productos
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS productos (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nombre VARCHAR(100),
                        precio DECIMAL(10, 2),
                        stock INT
                    )
                """)
        conexion.commit()
        
        #Tabla ventas
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS ventas (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        cliente_id INT,
                        producto_id INT,
                        cantidad INT,
                        fecha_venta DATE
                    )
                """)
        conexion.commit()
                
        cursor.close()
        conexion.close()

    def insertar_cliente(self, nombre, correo):
        conexion = self.crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO clientes (nombre, correo) VALUES (%s, %s)", (nombre, correo))
        conexion.commit()
        cursor.close()
        conexion.close()
        
    def insertar_producto(self, nombre, precio, stock):
        conexion = self.crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)", (nombre, precio, stock))
        conexion.commit()
        cursor.close()
        conexion.close()

    def insertar_venta(self, cliente_id, producto_id, cantidad, fecha_venta):
        conexion = self.crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO ventas (cliente_id, producto_id, cantidad, fecha_venta) VALUES (%s, %s, %s, %s)", (cliente_id, producto_id, cantidad, fecha_venta))
        conexion.commit()
        
        actualizar_stock = self.actualizar_stock(cantidad, producto_id)
        
        cursor.close()
        conexion.close()
    
    def actualizar_stock(self, cantidad, producto_id):
        conexion = self.crear_conexion()
        cursor = conexion.cursor()
        cursor.execute('''
        UPDATE productos 
        SET stock = %s 
        WHERE id = %s
        ''', (cantidad, producto_id))

        filas_modificadas = cursor.rowcount
        print(f"Filas modificadas: {filas_modificadas}")
        rta = input("Está seguro de querer confirmar la actualización? (Si):")
        if rta == "Si":
            conexion.commit()
        else:
            conexion.rollback()
        conexion.close()
    
    def consultar_tabla(self, tabla):
        conexion = self.crear_conexion()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM {tabla}")
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultados
    
    def obtener_clientes(self): 
        return self.consultar_tabla("clientes") 
    
    def obtener_productos(self):
        return self.consultar_tabla("productos")
    
    def consultar_ventas(self):
        conexion = self.crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT v.id, c.nombre AS cliente, p.nombre AS producto, v.cantidad, v.fecha_venta
            FROM ventas v
            JOIN clientes c ON v.cliente_id = c.id
            JOIN productos p ON v.producto_id = p.id
        """)
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultados
    
    def actualizar_cliente(self, cliente_id, nombre, correo):
        conexion = self.crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE clientes SET nombre = %s, correo = %s WHERE id = %s", (nombre, correo, cliente_id))
        conexion.commit()
        cursor.close()
        conexion.close()
        
    def actualizar_producto(self, producto_id, nombre, precio, stock):
        conexion = self.crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE productos SET nombre = %s, precio = %s, stock = %s WHERE id = %s", (nombre, precio, stock, producto_id))
        conexion.commit()
        cursor.close()
        conexion.close()
        
    def eliminar_venta(self, venta_id):
        conexion = self.crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM ventas WHERE id = %s", (venta_id,))
        venta_eliminada = cursor.rowcount
        if venta_eliminada > 0:
            print(f"Venta con ID {venta_id} eliminada correctamente.")
            conexion.commit()
        cursor.close()
        conexion.close()