from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """Ruta principal de la aplicación."""
    return jsonify({
        'mensaje': '¡Bienvenido a la aplicación Flask!',
        'estado': 'funcionando correctamente'
    })


@app.route('/health')
def health():
    """Endpoint de salud para verificar que la aplicación está corriendo."""
    return jsonify({'status': 'healthy'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

