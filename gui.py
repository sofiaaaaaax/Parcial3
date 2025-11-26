import tkinter as tk
from tkinter import ttk, messagebox
from logic import GestorNotas

class AplicacionNotas:
    """Interfaz gráfica para Gestión de Notas de Laboratorio"""
    
    def __init__(self, ventana, usuario=None, usuario_id=None, gestor_usuarios=None):
        self.ventana = ventana
        self.usuario = usuario
        self.usuario_id = usuario_id
        self.gestor_usuarios = gestor_usuarios
        self.ventana.title(f"Sistema de Gestión de Notas - Usuario: {usuario}")
        self.ventana.geometry("1000x700")
        self.ventana.configure(bg="#f0f0f0")
        
        self.gestor = GestorNotas(usuario_id)
        self.nota_seleccionada = None
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea la estructura principal de la interfaz"""
        
        # Frame superior para entrada de datos
        frame_entrada = ttk.LabelFrame(self.ventana, text="Nueva Nota", padding=10)
        frame_entrada.pack(fill=tk.X, padx=10, pady=10)
        
        # Título
        ttk.Label(frame_entrada, text="Título:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.entrada_titulo = ttk.Entry(frame_entrada, width=40)
        self.entrada_titulo.grid(row=0, column=1, padx=5, pady=5)
        
        # Categoría
        ttk.Label(frame_entrada, text="Categoría:").grid(row=0, column=2, sticky=tk.W, padx=5)
        self.entrada_categoria = ttk.Combobox(
            frame_entrada, 
            values=["General", "Experimento", "Resultados", "Observación"],
            width=15
        )
        self.entrada_categoria.set("General")
        self.entrada_categoria.grid(row=0, column=3, padx=5, pady=5)
        
        # Descripción
        ttk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, sticky=tk.NW, padx=5)
        self.entrada_desc = tk.Text(frame_entrada, width=70, height=4)
        self.entrada_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
        
        # Frame de botones
        frame_botones = ttk.Frame(frame_entrada)
        frame_botones.grid(row=2, column=0, columnspan=4, pady=10)
        
        ttk.Button(frame_botones, text="Agregar", command=self.agregar_nota).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Actualizar", command=self.actualizar_nota).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Limpiar", command=self.limpiar_campos).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Eliminar", command=self.eliminar_nota).pack(side=tk.LEFT, padx=5)
        
        # Frame de búsqueda
        frame_busqueda = ttk.Frame(self.ventana)
        frame_busqueda.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(frame_busqueda, text="Buscar:").pack(side=tk.LEFT, padx=5)
        self.entrada_busqueda = ttk.Entry(frame_busqueda, width=30)
        self.entrada_busqueda.pack(side=tk.LEFT, padx=5)
        self.entrada_busqueda.bind('<KeyRelease>', lambda e: self.filtrar_notas())
        
        ttk.Button(frame_busqueda, text="Limpiar búsqueda", command=self.limpiar_busqueda).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_busqueda, text="Cerrar Sesión", command=self.cerrar_sesion).pack(side=tk.RIGHT, padx=5)
        
        # Frame para la tabla de notas
        frame_tabla = ttk.LabelFrame(self.ventana, text="Notas Registradas", padding=10)
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_tabla)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Treeview para mostrar notas
        self.tabla_notas = ttk.Treeview(
            frame_tabla,
            columns=("ID", "Título", "Descripción", "Fecha", "Categoría"),
            height=15,
            yscrollcommand=scrollbar.set
        )
        scrollbar.config(command=self.tabla_notas.yview)
        
        # Configurar columnas
        self.tabla_notas.column("#0", width=0, stretch=tk.NO)
        self.tabla_notas.column("ID", anchor=tk.CENTER, width=40)
        self.tabla_notas.column("Título", anchor=tk.W, width=150)
        self.tabla_notas.column("Descripción", anchor=tk.W, width=300)
        self.tabla_notas.column("Fecha", anchor=tk.CENTER, width=150)
        self.tabla_notas.column("Categoría", anchor=tk.CENTER, width=100)
        
        # Encabezados
        self.tabla_notas.heading("#0", text="", anchor=tk.W)
        self.tabla_notas.heading("ID", text="ID", anchor=tk.CENTER)
        self.tabla_notas.heading("Título", text="Título", anchor=tk.W)
        self.tabla_notas.heading("Descripción", text="Descripción", anchor=tk.W)
        self.tabla_notas.heading("Fecha", text="Fecha", anchor=tk.CENTER)
        self.tabla_notas.heading("Categoría", text="Categoría", anchor=tk.CENTER)
        
        self.tabla_notas.pack(fill=tk.BOTH, expand=True)
        self.tabla_notas.bind('<<TreeviewSelect>>', self.seleccionar_nota)
        
        # Frame de estado
        self.label_estado = ttk.Label(self.ventana, text="Listo", relief=tk.SUNKEN)
        self.label_estado.pack(fill=tk.X, side=tk.BOTTOM)
    
    def agregar_nota(self):
        """Agrega una nueva nota"""
        titulo = self.entrada_titulo.get()
        descripcion = self.entrada_desc.get("1.0", tk.END).strip()
        categoria = self.entrada_categoria.get()
        
        exito, mensaje = self.gestor.agregar_nota(titulo, descripcion, categoria)
        
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.limpiar_campos()
            self.actualizar_tabla()
        else:
            messagebox.showerror("Error", mensaje)
    
    def actualizar_nota(self):
        """Actualiza la nota seleccionada"""
        if not self.nota_seleccionada:
            messagebox.showwarning("Advertencia", "Selecciona una nota para actualizar")
            return
        
        titulo = self.entrada_titulo.get()
        descripcion = self.entrada_desc.get("1.0", tk.END).strip()
        categoria = self.entrada_categoria.get()
        
        exito, mensaje = self.gestor.editar_nota(
            self.nota_seleccionada.id,
            titulo,
            descripcion,
            categoria
        )
        
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.limpiar_campos()
            self.actualizar_tabla()
        else:
            messagebox.showerror("Error", mensaje)
    
    def eliminar_nota(self):
        """Elimina la nota seleccionada"""
        if not self.nota_seleccionada:
            messagebox.showwarning("Advertencia", "Selecciona una nota para eliminar")
            return
        
        if messagebox.askyesno("Confirmar", f"¿Eliminar '{self.nota_seleccionada.titulo}'?"):
            exito, mensaje = self.gestor.eliminar_nota(self.nota_seleccionada.id)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
                self.limpiar_campos()
                self.actualizar_tabla()
    
    def seleccionar_nota(self, event):
        """Carga los datos de la nota seleccionada"""
        seleccion = self.tabla_notas.selection()
        if not seleccion:
            return
        
        item = seleccion[0]
        valores = self.tabla_notas.item(item, "values")
        nota_id = int(valores[0])
        
        self.nota_seleccionada = self.gestor.obtener_nota_por_id(nota_id)
        
        if self.nota_seleccionada:
            self.entrada_titulo.delete(0, tk.END)
            self.entrada_titulo.insert(0, self.nota_seleccionada.titulo)
            
            self.entrada_desc.delete("1.0", tk.END)
            self.entrada_desc.insert("1.0", self.nota_seleccionada.descripcion)
            
            self.entrada_categoria.set(self.nota_seleccionada.categoria)
            self.label_estado.config(text=f"Nota seleccionada: {self.nota_seleccionada}")
    
    def actualizar_tabla(self, notas=None):
        """Actualiza la tabla con las notas"""
        for item in self.tabla_notas.get_children():
            self.tabla_notas.delete(item)
        
        notas = notas or self.gestor.obtener_todas_notas()
        
        for nota in notas:
            desc_corta = nota.descripcion[:50] + "..." if len(nota.descripcion) > 50 else nota.descripcion
            self.tabla_notas.insert("", "end", values=(
                nota.id,
                nota.titulo,
                desc_corta,
                nota.fecha,
                nota.categoria
            ))
        
        self.label_estado.config(text=f"Total de notas: {len(notas)}")
    
    def filtrar_notas(self):
        """Filtra las notas según la búsqueda"""
        criterio = self.entrada_busqueda.get()
        
        if not criterio:
            self.actualizar_tabla()
            return
        
        resultados = self.gestor.buscar_notas(criterio)
        self.actualizar_tabla(resultados)
    
    def limpiar_busqueda(self):
        """Limpia el campo de búsqueda"""
        self.entrada_busqueda.delete(0, tk.END)
        self.actualizar_tabla()
    
    def limpiar_campos(self):
        """Limpia los campos de entrada"""
        self.entrada_titulo.delete(0, tk.END)
        self.entrada_desc.delete("1.0", tk.END)
        self.entrada_categoria.set("General")
        self.nota_seleccionada = None
        self.label_estado.config(text="Campos limpiados")
    
    def ejecutar(self):
        """Inicia la aplicación"""
        self.actualizar_tabla()
        self.ventana.mainloop()
    
    def cerrar_sesion(self):
        """Cierra la sesión del usuario"""
        if messagebox.askyesno("Cerrar Sesión", "¿Deseas cerrar la sesión?"):
            self.ventana.destroy()