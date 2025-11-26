#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Modelos de datos para el Sistema de Gestión de Notas
"""

from datetime import datetime

class Nota:
    """Modelo de datos para una nota de laboratorio"""
    
    def __init__(self, id=None, titulo="", descripcion="", fecha=None, categoria="General"):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.categoria = categoria
    
    def __str__(self):
        return f"ID: {self.id} - {self.titulo} ({self.categoria})"
    
    def __repr__(self):
        return f"Nota(id={self.id}, titulo='{self.titulo}', categoria='{self.categoria}')"
    
    def to_dict(self):
        """Convierte la nota a un diccionario"""
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'fecha': self.fecha,
            'categoria': self.categoria
        }
