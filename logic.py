from models import Nota
from database import ConexionDB
from datetime import datetime

class GestorNotas:
    """Gestor de notas con SQLite"""
    
    def __init__(self, usuario_id):
        self.db = ConexionDB()
        self.usuario_id = usuario_id
    
    def agregar_nota(self, titulo, descripcion, categoria="General"):
        """Agrega una nueva nota a la BD"""
        if not titulo.strip() or not descripcion.strip():
            return False, "El título y descripción no pueden estar vacíos"
        
        query = """
            INSERT INTO notas (usuario_id, titulo, descripcion, categoria)
            VALUES (?, ?, ?, ?)
        """
        
        exito = self.db.ejecutar_query(query, (self.usuario_id, titulo, descripcion, categoria))
        
        if exito:
            return True, f"Nota '{titulo}' agregada exitosamente"
        else:
            return False, "Error al agregar la nota"
    
    def obtener_todas_notas(self):
        """Obtiene todas las notas del usuario"""
        query = """
            SELECT id, titulo, descripcion, categoria, fecha_creacion, fecha_actualizacion
            FROM notas
            WHERE usuario_id = ?
            ORDER BY fecha_actualizacion DESC
        """
        resultados = self.db.obtener_todos(query, (self.usuario_id,))
        
        notas = []
        for row in resultados:
            nota = Nota(
                id=row['id'],
                titulo=row['titulo'],
                descripcion=row['descripcion'],
                fecha=row['fecha_actualizacion'],
                categoria=row['categoria']
            )
            notas.append(nota)
        
        return notas
    
    def obtener_nota_por_id(self, nota_id):
        """Obtiene una nota específica"""
        query = """
            SELECT id, titulo, descripcion, categoria, fecha_creacion, fecha_actualizacion
            FROM notas
            WHERE id = ? AND usuario_id = ?
        """
        resultado = self.db.obtener_uno(query, (nota_id, self.usuario_id))
        
        if resultado:
            return Nota(
                id=resultado['id'],
                titulo=resultado['titulo'],
                descripcion=resultado['descripcion'],
                fecha=resultado['fecha_actualizacion'],
                categoria=resultado['categoria']
            )
        return None
    
    def editar_nota(self, nota_id, titulo, descripcion, categoria="General"):
        """Edita una nota existente"""
        nota = self.obtener_nota_por_id(nota_id)
        if not nota:
            return False, "Nota no encontrada"
        
        if not titulo.strip() or not descripcion.strip():
            return False, "El título y descripción no pueden estar vacíos"
        
        query = """
            UPDATE notas
            SET titulo = ?, descripcion = ?, categoria = ?, fecha_actualizacion = CURRENT_TIMESTAMP
            WHERE id = ? AND usuario_id = ?
        """
        
        exito = self.db.ejecutar_query(query, (titulo, descripcion, categoria, nota_id, self.usuario_id))
        
        if exito:
            return True, f"Nota '{titulo}' actualizada exitosamente"
        else:
            return False, "Error al actualizar la nota"
    
    def eliminar_nota(self, nota_id):
        """Elimina una nota"""
        nota = self.obtener_nota_por_id(nota_id)
        if not nota:
            return False, "Nota no encontrada"
        
        query = "DELETE FROM notas WHERE id = ? AND usuario_id = ?"
        exito = self.db.ejecutar_query(query, (nota_id, self.usuario_id))
        
        if exito:
            return True, f"Nota '{nota.titulo}' eliminada exitosamente"
        else:
            return False, "Error al eliminar la nota"
    
    def buscar_notas(self, criterio):
        """Busca notas por título o descripción"""
        query = """
            SELECT id, titulo, descripcion, categoria, fecha_creacion, fecha_actualizacion
            FROM notas
            WHERE usuario_id = ? AND (titulo LIKE ? OR descripcion LIKE ?)
            ORDER BY fecha_actualizacion DESC
        """
        
        criterio_busqueda = f"%{criterio}%"
        resultados = self.db.obtener_todos(query, (self.usuario_id, criterio_busqueda, criterio_busqueda))
        
        notas = []
        for row in resultados:
            nota = Nota(
                id=row['id'],
                titulo=row['titulo'],
                descripcion=row['descripcion'],
                fecha=row['fecha_actualizacion'],
                categoria=row['categoria']
            )
            notas.append(nota)
        
        return notas
    
    def filtrar_por_categoria(self, categoria):
        """Filtra notas por categoría"""
        query = """
            SELECT id, titulo, descripcion, categoria, fecha_creacion, fecha_actualizacion
            FROM notas
            WHERE usuario_id = ? AND categoria = ?
            ORDER BY fecha_actualizacion DESC
        """
        
        resultados = self.db.obtener_todos(query, (self.usuario_id, categoria))
        
        notas = []
        for row in resultados:
            nota = Nota(
                id=row['id'],
                titulo=row['titulo'],
                descripcion=row['descripcion'],
                fecha=row['fecha_actualizacion'],
                categoria=row['categoria']
            )
            notas.append(nota)
        
        return notas
    
    def obtener_categorias(self):
        """Obtiene categorías únicas del usuario"""
        query = """
            SELECT DISTINCT categoria FROM notas
            WHERE usuario_id = ?
            ORDER BY categoria
        """
        
        resultados = self.db.obtener_todos(query, (self.usuario_id,))
        return [row['categoria'] for row in resultados]
    
    def exportar_datos(self):
        """Exporta todas las notas como diccionarios"""
        notas = self.obtener_todas_notas()
        return [nota.to_dict() for nota in notas]
    
    def obtener_estadisticas(self):
        """Obtiene estadísticas de las notas del usuario"""
        query = "SELECT COUNT(*) as total, COUNT(DISTINCT categoria) as categorias FROM notas WHERE usuario_id = ?"
        resultado = self.db.obtener_uno(query, (self.usuario_id,))
        return resultado
    
    def cerrar_conexion(self):
        """Cierra la conexión a la BD"""
        self.db.cerrar_conexion()