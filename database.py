import sqlite3
import os
from datetime import datetime

class ConexionDB:
    """Gestor de conexión a base de datos SQLite"""
    
    def __init__(self, nombre_db="lab_notas.db"):
        self.nombre_db = nombre_db
        self.conexion = None
        self.crear_conexion()
        self.crear_tablas()
    
    def crear_conexion(self):
        """Crea conexión a la base de datos"""
        try:
            self.conexion = sqlite3.connect(self.nombre_db)
            self.conexion.row_factory = sqlite3.Row
            print(f"[OK] Conectado a la base de datos: {self.nombre_db}")
        except sqlite3.Error as e:
            print(f"[ERROR] Error en conexion: {e}")
    
    def crear_tablas(self):
        """Crea las tablas si no existen"""
        cursor = self.conexion.cursor()
        
        # Tabla de usuarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                contraseña TEXT NOT NULL,
                fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                activo INTEGER DEFAULT 1
            )
        ''')
        
        # Tabla de notas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                titulo TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                categoria TEXT DEFAULT 'General',
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (usuario_id) REFERENCES usuarios (id) ON DELETE CASCADE
            )
        ''')
        
        self.conexion.commit()
        print("[OK] Tablas creadas exitosamente")
    
    def cerrar_conexion(self):
        """Cierra la conexión a la base de datos"""
        if self.conexion:
            self.conexion.close()
            print("[OK] Conexion cerrada")
    
    def ejecutar_query(self, query, parametros=()):
        """Ejecuta una query sin retorno"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(query, parametros)
            self.conexion.commit()
            return True
        except sqlite3.Error as e:
            print(f"[ERROR] Error en query: {e}")
            return False
    
    def obtener_uno(self, query, parametros=()):
        """Obtiene un registro"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(query, parametros)
            return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"[ERROR] Error en query: {e}")
            return None
    
    def obtener_todos(self, query, parametros=()):
        """Obtiene todos los registros"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(query, parametros)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"[ERROR] Error en query: {e}")
            return []
    
    def obtener_ultimo_id(self):
        """Obtiene el ID del último registro insertado"""
        cursor = self.conexion.cursor()
        cursor.execute("SELECT last_insert_rowid()")
        return cursor.fetchone()[0]