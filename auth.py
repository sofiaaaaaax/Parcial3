import hashlib
from database import ConexionDB

class GestorUsuarios:
    """Gestor de usuarios con SQLite"""
    
    def __init__(self):
        self.db = ConexionDB()
        self.crear_usuarios_demo()
    
    def crear_usuarios_demo(self):
        """Crea usuarios de demostración si no existen"""
        usuarios_demo = [
            ("admin", "admin123"),
            ("demo", "demo123")
        ]
        
        for usuario, contraseña in usuarios_demo:
            if not self.usuario_existe(usuario):
                self.registrar_usuario(usuario, contraseña)
    
    def hashear_contraseña(self, contraseña):
        """Hashea una contraseña usando SHA-256"""
        return hashlib.sha256(contraseña.encode()).hexdigest()
    
    def registrar_usuario(self, usuario, contraseña):
        """Registra un nuevo usuario en la BD"""
        if self.usuario_existe(usuario):
            return False, "El usuario ya existe"
        
        if len(contraseña) < 6:
            return False, "La contraseña debe tener al menos 6 caracteres"
        
        if len(usuario) < 3:
            return False, "El usuario debe tener al menos 3 caracteres"
        
        contraseña_hash = self.hashear_contraseña(contraseña)
        
        query = "INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)"
        exito = self.db.ejecutar_query(query, (usuario, contraseña_hash))
        
        if exito:
            return True, "Usuario registrado exitosamente"
        else:
            return False, "Error al registrar usuario"
    
    def autenticar(self, usuario, contraseña):
        """Autentica un usuario"""
        query = "SELECT id, contraseña FROM usuarios WHERE usuario = ? AND activo = 1"
        resultado = self.db.obtener_uno(query, (usuario,))
        
        if not resultado:
            return False, "Usuario o contraseña incorrectos"
        
        contraseña_hash = self.hashear_contraseña(contraseña)
        
        if resultado['contraseña'] == contraseña_hash:
            return True, resultado['id']
        else:
            return False, "Usuario o contraseña incorrectos"
    
    def usuario_existe(self, usuario):
        """Verifica si un usuario existe"""
        query = "SELECT id FROM usuarios WHERE usuario = ?"
        resultado = self.db.obtener_uno(query, (usuario,))
        return resultado is not None
    
    def obtener_id_usuario(self, usuario):
        """Obtiene el ID del usuario"""
        query = "SELECT id FROM usuarios WHERE usuario = ?"
        resultado = self.db.obtener_uno(query, (usuario,))
        return resultado['id'] if resultado else None
    
    def obtener_usuario_por_id(self, usuario_id):
        """Obtiene el nombre del usuario por ID"""
        query = "SELECT usuario FROM usuarios WHERE id = ?"
        resultado = self.db.obtener_uno(query, (usuario_id,))
        return resultado['usuario'] if resultado else None
    
    def cerrar_conexion(self):
        """Cierra la conexión a la BD"""
        self.db.cerrar_conexion()