from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import subprocess
from user_management import registrar_usuario, login_usuario, guardar_descubrimiento, obtener_descubrimientos, leer_usuarios, escribir_usuarios
import pandas as pd

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Ensure this is a secure, random value

# Load animal data from the CSV
animales_df = pd.read_csv('animales.csv')
animales_info = animales_df.set_index('marker_id').T.to_dict()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'login' in request.form:
            username = request.form['username']
            password = request.form['password']
            
            if username == 'Admin':
                return 'El administrador no puede iniciar sesión a través del formulario. Use la opción de acceso por cámara.'

            if login_usuario(username, password):
                session['username'] = username
                return redirect(url_for('main'))
            else:
                return 'Inicio de sesión fallido. Inténtalo de nuevo.'
        elif 'camera_login' in request.form:
            result = subprocess.run(['python3', 'face_recognition_login.py'], capture_output=True, text=True)
            if "ACCESS_GRANTED" in result.stdout:
                session['username'] = 'Admin'
                return redirect(url_for('main'))
            else:
                return 'Reconocimiento facial fallido. Inténtalo de nuevo.'

    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        if username.lower() == 'admin':
            return 'No puedes registrar un usuario con el nombre de "admin".'

        resultado = registrar_usuario(username, password, firstname, lastname, email)
        if resultado == "Usuario registrado con éxito":
            return redirect(url_for('index'))
        else:
            return 'Registro fallido. ' + resultado

    return render_template('register.html')

@app.route('/main', methods=['GET'])
def main():
    username = session.get('username')
    descubrimientos = obtener_descubrimientos(username)
    animales = {
        '0': 'static/images/Koala.png',
        '1': 'static/images/Leon.png',
        '2': 'static/images/Elefante.png',
        '3': 'static/images/Pinguino.png',
        '4': 'static/images/Buho.png',
        '5': 'static/images/Murcielago.png'
    }
    imagenes_descubiertas = {id: animales[id] for id in descubrimientos if id in animales}
    return render_template('main.html', username=username, imagenes_descubiertas=imagenes_descubiertas)

@app.route('/animal/<animal_id>', methods=['GET'])
def animal(animal_id):
    animal_info = animales_info.get(int(animal_id))
    if not animal_info:
        return 'Animal no encontrado', 404
    animal_info['nombre'] = animal_info['nombre'].replace(" ", "").lower()
    return render_template('animal.html', animal=animal_info)

@app.route('/run_script', methods=['POST'])
def run_script():
    username = session.get('username')
    if not username:
        return redirect(url_for('index'))

    script_path = 'safarivirtual.py'
    result = subprocess.run(['python3', script_path], capture_output=True, text=True)
    
    for line in result.stdout.splitlines():
        if line.startswith("DESCUBIERTO:"):
            animal_id = line.split(":")[1].strip()
            guardar_descubrimiento(username, animal_id)

    return redirect(url_for('main'))

@app.route('/tutorial', methods=['GET'])
def tutorial():
    username = session.get('username')
    return render_template('tutorial.html', username=username)

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/manage_users', methods=['GET'])
def manage_users():
    if session.get('username') != 'Admin':
        return redirect(url_for('index'))

    usuarios = leer_usuarios()
    animales = {
        '0': 'static/images/Koala.png',
        '1': 'static/images/Leon.png',
        '2': 'static/images/Elefante.png',
        '3': 'static/images/Pinguino.png',
        '4': 'static/images/Buho.png',
        '5': 'static/images/Murcielago.png'
    }

    for usuario in usuarios:
        usuario['descubrimientos'] = usuario['descubrimientos'].split(',') if usuario['descubrimientos'] else []

    return render_template('manage_users.html', usuarios=usuarios, animales=animales)

@app.route('/remove_discovery', methods=['POST'])
def remove_discovery():
    data = request.get_json()
    username = data.get('username')
    animal_id = data.get('animal_id')

    usuarios = leer_usuarios()
    for usuario in usuarios:
        if usuario['username'] == username:
            descubrimientos = usuario['descubrimientos'].split(',')
            if animal_id in descubrimientos:
                descubrimientos.remove(animal_id)
                usuario['descubrimientos'] = ','.join(descubrimientos)
                break
    escribir_usuarios(usuarios)
    return jsonify({'success': True})

@app.route('/delete_user', methods=['POST'])
def delete_user():
    data = request.get_json()
    username = data.get('username')

    usuarios = leer_usuarios()
    usuarios = [usuario for usuario in usuarios if usuario['username'] != username]
    escribir_usuarios(usuarios)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
