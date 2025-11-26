#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Gestión de Notas de Laboratorio
Aplicación desarrollada con Python y Tkinter
Autor: [Tu nombre]
Fecha: 2025
"""

import tkinter as tk
from tkinter import messagebox
from auth import GestorUsuarios
from gui import AplicacionNotas

class VentanaLogin:
    """Ventana de login y registro"""
    
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.gestor_usuarios = GestorUsuarios()
        self.usuario_actual = None
        self.usuario_id = None
        
        self.ventana_principal.title("Login - Sistema de Gestión de Notas")
        self.ventana_principal.geometry("400x350")
        self.ventana_principal.configure(bg="#f0f0f0")
        self.centrar_ventana()
        
        self.crear_interfaz_login()
    
    def centrar_ventana(self):
        """Centra la ventana en la pantalla"""
        self.ventana_principal.update_idletasks()
        ancho = self.ventana_principal.winfo_width()
        alto = self.ventana_principal.winfo_height()
        x = (self.ventana_principal.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.ventana_principal.winfo_screenheight() // 2) - (alto // 2)
        self.ventana_principal.geometry(f"{ancho}x{alto}+{x}+{y}")
    
    def crear_interfaz_login(self):
        """Crea la interfaz de login"""
        # Frame principal
        frame_principal = tk.Frame(self.ventana_principal, bg="#ffffff")
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        titulo = tk.Label(
            frame_principal,
            text="Gestión de Notas\nde Laboratorio",
            font=("Arial", 20, "bold"),
            bg="#ffffff",
            fg="#333333"
        )
        titulo.pack(pady=20)
        
        # Frame para login
        self.frame_login = tk.Frame(frame_principal, bg="#ffffff")
        self.frame_login.pack(fill=tk.BOTH, expand=True)
        
        # Usuario
        tk.Label(
            self.frame_login,
            text="Usuario:",
            font=("Arial", 10),
            bg="#ffffff"
        ).pack(anchor=tk.W, pady=(10, 0))
        
        self.entrada_usuario = tk.Entry(
            self.frame_login,
            font=("Arial", 11),
            width=30,
            relief=tk.FLAT,
            bg="#f5f5f5"
        )
        self.entrada_usuario.pack(pady=5, ipady=5)
        self.entrada_usuario.bind('<Return>', lambda e: self.iniciar_sesion())
        
        # Contraseña
        tk.Label(
            self.frame_login,
            text="Contraseña:",
            font=("Arial", 10),
            bg="#ffffff"
        ).pack(anchor=tk.W, pady=(10, 0))
        
        self.entrada_contraseña = tk.Entry(
            self.frame_login,
            font=("Arial", 11),
            width=30,
            show="•",
            relief=tk.FLAT,
            bg="#f5f5f5"
        )
        self.entrada_contraseña.pack(pady=5, ipady=5)
        self.entrada_contraseña.bind('<Return>', lambda e: self.iniciar_sesion())
        
        # Frame de botones
        frame_botones = tk.Frame(self.frame_login, bg="#ffffff")
        frame_botones.pack(pady=20)
        
        tk.Button(
            frame_botones,
            text="Iniciar Sesión",
            font=("Arial", 10, "bold"),
            bg="#4CAF50",
            fg="white",
            width=20,
            cursor="hand2",
            relief=tk.FLAT,
            command=self.iniciar_sesion
        ).pack(pady=5)
        
        tk.Button(
            frame_botones,
            text="Registrarse",
            font=("Arial", 10, "bold"),
            bg="#2196F3",
            fg="white",
            width=20,
            cursor="hand2",
            relief=tk.FLAT,
            command=self.mostrar_registro
        ).pack(pady=5)
        
        # Info de usuarios de prueba
        info = tk.Label(
            self.frame_login,
            text="Usuarios de prueba:\nadmin / admin123\ndemo / demo123",
            font=("Arial", 8),
            bg="#ffffff",
            fg="#666666"
        )
        info.pack(pady=10)
        
        self.entrada_usuario.focus()
    
    def iniciar_sesion(self):
        """Autentica al usuario"""
        usuario = self.entrada_usuario.get().strip()
        contraseña = self.entrada_contraseña.get()
        
        if not usuario or not contraseña:
            messagebox.showwarning("Advertencia", "Completa todos los campos")
            return
        
        exito, resultado = self.gestor_usuarios.autenticar(usuario, contraseña)
        
        if exito:
            self.usuario_actual = usuario
            self.usuario_id = resultado  # ID del usuario
            self.abrir_aplicacion_principal()
        else:
            messagebox.showerror("Error", resultado)
            self.entrada_contraseña.delete(0, tk.END)
    
    def mostrar_registro(self):
        """Muestra la interfaz de registro"""
        self.frame_login.destroy()
        
        self.frame_registro = tk.Frame(self.ventana_principal, bg="#ffffff")
        self.frame_registro.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(
            self.frame_registro,
            text="Crear Nueva Cuenta",
            font=("Arial", 14, "bold"),
            bg="#ffffff"
        ).pack(pady=15)
        
        # Usuario
        tk.Label(
            self.frame_registro,
            text="Nuevo Usuario:",
            font=("Arial", 10),
            bg="#ffffff"
        ).pack(anchor=tk.W, padx=20, pady=(10, 0))
        
        self.entrada_nuevo_usuario = tk.Entry(
            self.frame_registro,
            font=("Arial", 11),
            width=30,
            relief=tk.FLAT,
            bg="#f5f5f5"
        )
        self.entrada_nuevo_usuario.pack(padx=20, pady=5, ipady=5)
        
        # Contraseña
        tk.Label(
            self.frame_registro,
            text="Contraseña (min. 6 caracteres):",
            font=("Arial", 10),
            bg="#ffffff"
        ).pack(anchor=tk.W, padx=20, pady=(10, 0))
        
        self.entrada_nueva_contraseña = tk.Entry(
            self.frame_registro,
            font=("Arial", 11),
            width=30,
            show="•",
            relief=tk.FLAT,
            bg="#f5f5f5"
        )
        self.entrada_nueva_contraseña.pack(padx=20, pady=5, ipady=5)
        
        # Confirmar contraseña
        tk.Label(
            self.frame_registro,
            text="Confirmar Contraseña:",
            font=("Arial", 10),
            bg="#ffffff"
        ).pack(anchor=tk.W, padx=20, pady=(10, 0))
        
        self.entrada_confirmar = tk.Entry(
            self.frame_registro,
            font=("Arial", 11),
            width=30,
            show="•",
            relief=tk.FLAT,
            bg="#f5f5f5"
        )
        self.entrada_confirmar.pack(padx=20, pady=5, ipady=5)
        
        # Botones
        frame_botones = tk.Frame(self.frame_registro, bg="#ffffff")
        frame_botones.pack(pady=20)
        
        tk.Button(
            frame_botones,
            text="Registrarse",
            font=("Arial", 10, "bold"),
            bg="#4CAF50",
            fg="white",
            width=20,
            cursor="hand2",
            relief=tk.FLAT,
            command=self.registrar_usuario
        ).pack(pady=5)
        
        tk.Button(
            frame_botones,
            text="Volver",
            font=("Arial", 10, "bold"),
            bg="#f44336",
            fg="white",
            width=20,
            cursor="hand2",
            relief=tk.FLAT,
            command=self.volver_login
        ).pack(pady=5)
    
    def registrar_usuario(self):
        """Registra un nuevo usuario"""
        usuario = self.entrada_nuevo_usuario.get().strip()
        contraseña = self.entrada_nueva_contraseña.get()
        confirmar = self.entrada_confirmar.get()
        
        if not usuario or not contraseña or not confirmar:
            messagebox.showwarning("Advertencia", "Completa todos los campos")
            return
        
        if contraseña != confirmar:
            messagebox.showerror("Error", "Las contraseñas no coinciden")
            return
        
        exito, mensaje = self.gestor_usuarios.registrar_usuario(usuario, contraseña)
        
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.volver_login()
        else:
            messagebox.showerror("Error", mensaje)
    
    def volver_login(self):
        """Vuelve a la pantalla de login"""
        self.frame_registro.destroy()
        self.crear_interfaz_login()
    
    def abrir_aplicacion_principal(self):
        """Abre la aplicación principal"""
        self.ventana_principal.destroy()
        
        ventana_app = tk.Tk()
        app = AplicacionNotas(ventana_app, self.usuario_actual, self.usuario_id, self.gestor_usuarios)
        app.ejecutar()

def main():
    """Función principal que inicia la aplicación"""
    ventana = tk.Tk()
    login = VentanaLogin(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()