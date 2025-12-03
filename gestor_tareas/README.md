# 📋 Gestor de Tareas

Aplicación web simple para gestionar tareas desarrollada con Flask. Permite agregar, listar y marcar tareas como completadas, con persistencia de datos en archivo JSON.

## 🚀 Características

- ✅ Agregar nuevas tareas
- ✅ Marcar tareas como completadas o desmarcarlas
- ✅ Lista ordenada: tareas incompletas primero, luego completadas
- ✅ Persistencia de datos en archivo JSON
- ✅ Interfaz web simple y moderna
- ✅ Sin base de datos: almacenamiento en archivo local

## 📋 Requisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## 🔧 Instalación

1. **Clona o descarga el proyecto**

```bash
cd gestor_tareas
```

2. **Crea un entorno virtual (recomendado)**

```bash
python -m venv venv
```

3. **Activa el entorno virtual**

En macOS/Linux:
```bash
source venv/bin/activate
```

En Windows:
```bash
venv\Scripts\activate
```

4. **Instala las dependencias**

```bash
pip install -r requirements.txt
```

## 🎯 Uso

1. **Inicia la aplicación**

```bash
python app.py
```

2. **Abre tu navegador**

Navega a: `http://localhost:5000`

3. **Gestiona tus tareas**

- Escribe una nueva tarea en el formulario y haz clic en "Agregar"
- Haz clic en "[Completar]" para marcar una tarea como completada
- Las tareas completadas aparecen tachadas y al final de la lista

## 📁 Estructura del Proyecto

```
gestor_tareas/
├── app.py                 # Aplicación Flask principal
├── requirements.txt       # Dependencias del proyecto
├── tareas.json           # Archivo de persistencia (se crea automáticamente)
├── templates/
│   └── index.html        # Plantilla HTML
├── .gitignore            # Archivos ignorados por Git
└── README.md             # Este archivo
```

## 🛠️ Tecnologías Utilizadas

- **Flask 3.0.0**: Framework web de Python
- **Jinja2**: Motor de plantillas (incluido con Flask)
- **JSON**: Formato de almacenamiento de datos
- **HTML/CSS**: Interfaz de usuario

## 📝 Funcionalidades Técnicas

### Rutas Disponibles

- `GET /`: Muestra la lista de tareas y el formulario
- `POST /agregar`: Agrega una nueva tarea
- `GET /completar/<id>`: Marca/desmarca una tarea como completada

### Persistencia

Las tareas se guardan automáticamente en el archivo `tareas.json` después de cada operación (agregar o completar). El archivo se crea automáticamente la primera vez que agregas una tarea.

### Formato de Datos

Cada tarea se almacena como un diccionario con la siguiente estructura:

```json
{
  "id": 1,
  "texto": "Tarea de ejemplo",
  "hecho": false
}
```

## 🔒 Notas de Seguridad

- Esta aplicación está diseñada para uso local o en entornos de desarrollo
- No incluye autenticación ni autorización
- Para producción, considera agregar medidas de seguridad adicionales

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso personal y educativo.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.

## 📧 Soporte

Si encuentras algún problema o tienes sugerencias, por favor abre un issue en el repositorio del proyecto.

