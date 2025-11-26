# 📝 Sistema de Gestión de Notas de Laboratorio

Sistema desarrollado en Python con Tkinter para la gestión de notas de laboratorio con autenticación de usuarios y base de datos SQLite.

**Creado por:** Ricardo Jaraba Gallego  
**Presentado a:** Profesor Feiberth Alirio  
**Curso:** Lenguajes de Programación 2025-2  
**Parcial:** 3

---

## � Instalación desde GitHub

### **Paso 1: Clonar el Repositorio**

Abre una terminal o CMD y ejecuta:

```bash
git clone [URL_DEL_REPOSITORIO]
cd "parcial 3"
```

### **Paso 2: Verificar Python**

Asegúrate de tener Python 3.x instalado:

```bash
python --version
```

Si no lo tienes instalado, descárgalo desde [python.org](https://www.python.org/downloads/)

### **Paso 3: Ejecutar la Aplicación**

```bash
python main.py
```

¡Eso es todo! No se requieren dependencias externas ya que todas las librerías usadas vienen incluidas con Python.

---

## �🚀 Cómo Ejecutar el Código

### **Requisitos Previos**
- Python 3.x instalado en tu sistema
- Tkinter (incluido por defecto en Python)
- SQLite3 (incluido por defecto en Python)

### **Método 1: Desde la Terminal/CMD**

1. Abre una terminal o CMD
2. Navega hasta la carpeta del proyecto:
   ```bash
   cd "ruta/a/parcial 3"
   ```
3. Ejecuta el programa:
   ```bash
   python main.py
   ```

### **Método 2: Desde VS Code**

1. Abre la carpeta del proyecto en VS Code
2. Abre el archivo `main.py`
3. Presiona `F5` o ejecuta desde la terminal integrada:
   ```bash
   python main.py
   ```

### **Método 3: Doble Clic**

Simplemente haz doble clic en el archivo `main.py` desde el explorador de archivos.

---

## 🔐 Credenciales de Acceso

El sistema cuenta con dos usuarios de prueba preconfigurados que se crean automáticamente:

### **Usuario Administrador**
- **Usuario:** `admin`
- **Contraseña:** `admin123`

### **Usuario Demo**
- **Usuario:** `demo`
- **Contraseña:** `demo123`

También puedes crear tu propio usuario haciendo clic en el botón **"Registrarse"** en la pantalla de login.

---

## 📋 Funcionalidades

- ✅ **Autenticación de usuarios** con contraseñas encriptadas (SHA-256)
- ✅ **Crear notas** con título, descripción y categoría
- ✅ **Editar notas** existentes
- ✅ **Eliminar notas** con confirmación
- ✅ **Buscar notas** por título o descripción
- ✅ **Filtrar por categoría** (General, Experimento, Resultados, Observación)
- ✅ **Registro de nuevos usuarios**
- ✅ **Base de datos SQLite** para persistencia de datos
- ✅ **Interfaz gráfica intuitiva** con Tkinter
- ✅ **Sistema multiusuario** - Cada usuario solo ve sus propias notas

---

## 📁 Estructura del Proyecto

```
parcial 3/
│
├── main.py           # Punto de entrada de la aplicación (Login)
├── auth.py           # Gestión de autenticación de usuarios
├── database.py       # Conexión y gestión de base de datos SQLite
├── gui.py            # Interfaz gráfica de usuario
├── logic.py          # Lógica de negocio para gestión de notas
├── models.py         # Modelos de datos (Nota)
├── requirements.txt  # Dependencias del proyecto
├── .gitignore        # Archivos ignorados por Git
└── README.md         # Este archivo
```

**Nota:** El archivo `lab_notas.db` se crea automáticamente al ejecutar la aplicación por primera vez.

---

## 💾 Base de Datos

El sistema utiliza **SQLite** para almacenar la información. La base de datos `lab_notas.db` se crea automáticamente la primera vez que ejecutas el programa.

### **Tablas:**

1. **usuarios**
   - `id` - Identificador único
   - `usuario` - Nombre de usuario (único)
   - `contraseña` - Contraseña encriptada con SHA-256
   - `fecha_registro` - Fecha de creación de la cuenta
   - `activo` - Estado del usuario

2. **notas**
   - `id` - Identificador único
   - `usuario_id` - Referencia al usuario propietario
   - `titulo` - Título de la nota
   - `descripcion` - Contenido de la nota
   - `categoria` - Categoría de la nota
   - `fecha_creacion` - Fecha de creación
   - `fecha_actualizacion` - Última modificación

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x** - Lenguaje de programación principal
- **Tkinter** - Interfaz gráfica de usuario (GUI)
- **SQLite3** - Base de datos relacional
- **Hashlib** - Encriptación de contraseñas con SHA-256

Todas estas bibliotecas vienen incluidas con Python, por lo que **no necesitas instalar nada adicional**.

---

## 📝 Uso de la Aplicación

### **1. Inicio de Sesión**
Al ejecutar el programa, verás la pantalla de login donde puedes:
- Iniciar sesión con un usuario existente
- Registrar un nuevo usuario

### **2. Gestión de Notas**
Una vez iniciada la sesión, puedes:
- **Agregar una nota:** Completa el título, descripción y categoría, luego haz clic en "Agregar"
- **Editar una nota:** Selecciona una nota de la tabla, modifica los campos y haz clic en "Actualizar"
- **Eliminar una nota:** Selecciona una nota y haz clic en "Eliminar"
- **Buscar notas:** Usa el campo de búsqueda para filtrar por título o descripción
- **Limpiar formulario:** Haz clic en "Limpiar" para vaciar los campos

### **3. Cerrar Sesión**
Haz clic en el botón "Cerrar Sesión" para volver a la pantalla de login.

---

## 🔒 Seguridad

- Las contraseñas se almacenan encriptadas usando **SHA-256**
- Cada usuario solo puede acceder a sus propias notas
- El sistema valida las credenciales antes de permitir el acceso
- Las contraseñas deben tener al menos 6 caracteres
- Los nombres de usuario deben tener al menos 3 caracteres

---

## 📸 Capturas de Pantalla

### Pantalla de Login
La interfaz de autenticación permite iniciar sesión o registrarse.

### Gestión de Notas
Interfaz principal con tabla de notas, formularios de entrada y opciones de búsqueda.

---

## ⚠️ Notas Importantes

- La base de datos (`lab_notas.db`) se crea automáticamente en la primera ejecución
- Los usuarios de prueba (`admin` y `demo`) se crean automáticamente
- No se requiere instalación de dependencias adicionales
- El programa funciona en Windows, Linux y macOS

---

## 🐛 Solución de Problemas

### **El programa no inicia**
- Verifica que Python 3.x esté instalado correctamente
- Asegúrate de estar en la carpeta correcta del proyecto

### **Error de Tkinter**
- En Linux, instala tkinter: `sudo apt-get install python3-tk`
- En Windows/Mac, tkinter viene incluido con Python

### **No puedo crear usuarios**
- Verifica que tengas permisos de escritura en la carpeta del proyecto
- La base de datos debe poder crearse en la misma carpeta

---

## 👨‍💻 Autor

**Ricardo Jaraba Gallego**  
Universidad - Lenguajes de Programación 2025-2  
Parcial 3  
Profesor: Feiberth Alirio

---

## 📞 Contacto

Para cualquier consulta o problema con el proyecto, contactar al autor.

---

## 📄 Licencia

Proyecto educativo - Universidad 2025  
Desarrollado como ejercicio académico para la asignatura de Lenguajes de Programación
