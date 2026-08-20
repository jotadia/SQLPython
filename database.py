# -*- coding: utf-8 -*-
"""
Created on 19 aug 2026

@author: JCOD
"""
import mysql.connector

class MyDataBase:
    VERSION = "1.0"

    def __init__(self, host="localhost", user="root",
                 password="Root", database="mystore") -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None

    def crear_conexion(self):
        self.conexion = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            use_pure=True,
        )
        return self.conexion

    def cerrar(self) -> None:
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()

    def __str__(self) -> str:
        return f"MyDataBase({self.user}@{self.host}/{self.database}) v{self.VERSION}"