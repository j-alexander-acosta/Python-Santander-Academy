from flask import Flask, request, redirect, render_template
import json
import os

app = Flask(__name__)

# Archivo JSON para persistencia
ARCHIVO_TAREAS = 'tareas.json'

# Lista global en memoria para almacenar las tareas
tareas = []
contador_id = 1

def cargar_tareas():
    """Carga las tareas desde el archivo JSON."""
    global tareas, contador_id
    if os.path.exists(ARCHIVO_TAREAS):
        try:
            with open(ARCHIVO_TAREAS, 'r', encoding='utf-8') as f:
                tareas = json.load(f)
            # Actualizar contador_id al máximo ID + 1
            if tareas:
                contador_id = max(tarea['id'] for tarea in tareas) + 1
            else:
                contador_id = 1
        except (json.JSONDecodeError, IOError):
            tareas = []
            contador_id = 1
    else:
        tareas = []
        contador_id = 1

def guardar_tareas():
    """Guarda las tareas en el archivo JSON."""
    try:
        with open(ARCHIVO_TAREAS, 'w', encoding='utf-8') as f:
            json.dump(tareas, f, ensure_ascii=False, indent=2)
    except IOError:
        pass  # Manejar error de escritura silenciosamente

def agregar_tarea(texto):
    """Agrega una nueva tarea a la lista global con un ID incremental."""
    global contador_id
    if texto and texto.strip():
        nueva_tarea = {
            'id': contador_id,
            'texto': texto.strip(),
            'hecho': False
        }
        tareas.append(nueva_tarea)
        contador_id += 1
        guardar_tareas()
        return nueva_tarea
    return None

def completar_tarea(id):
    """Marca o desmarca una tarea como completada según su ID."""
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['hecho'] = not tarea['hecho']
            guardar_tareas()
            return tarea
    return None

@app.route('/')
def index():
    # Ordenar tareas: incompletas primero, luego completadas
    tareas_ordenadas = sorted(tareas, key=lambda t: t['hecho'])
    return render_template('index.html', tareas=tareas_ordenadas)

@app.route('/agregar', methods=['POST'])
def agregar():
    texto_tarea = request.form.get('texto_tarea')
    if texto_tarea:
        agregar_tarea(texto_tarea)
    return redirect('/')

@app.route('/completar/<int:id>')
def completar(id):
    completar_tarea(id)
    return redirect('/')

if __name__ == '__main__':
    # Cargar tareas al iniciar la aplicación
    cargar_tareas()
    app.run(debug=True, host='0.0.0.0', port=5000)

