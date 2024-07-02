import csv
import hashlib

# Función para leer usuarios desde el archivo CSV
def leer_usuarios():
    usuarios = []
    try:
        with open('usuarios.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'descubrimientos' not in row:
                    row['descubrimientos'] = ''
                usuarios.append(row)
    except FileNotFoundError:
        pass  # El archivo no existe aún, lo crearemos cuando registremos el primer usuario
    return usuarios

# Función para escribir usuarios al archivo CSV
def escribir_usuarios(usuarios):
    fieldnames = ['username', 'password', 'firstname', 'lastname', 'email', 'descubrimientos']
    with open('usuarios.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(usuarios)

# Función para escribir un solo usuario al archivo CSV
def escribir_usuario(usuario):
    usuarios = leer_usuarios()
    usuarios.append(usuario)
    escribir_usuarios(usuarios)

# Función para registrar un nuevo usuario
def registrar_usuario(username, password, firstname, lastname, email):
    usuarios = leer_usuarios()
    for usuario in usuarios:
        if usuario['username'] == username:
            return "El usuario ya existe"
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    nuevo_usuario = {
        'username': username,
        'password': password_hash,
        'firstname': firstname,
        'lastname': lastname,
        'email': email,
        'descubrimientos': ''
    }
    escribir_usuario(nuevo_usuario)
    return "Usuario registrado con éxito"

# Función para hacer login
def login_usuario(username, password):
    usuarios = leer_usuarios()
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    for usuario in usuarios:
        if usuario['username'] == username and usuario['password'] == password_hash:
            return True
    return False

# Función para guardar un descubrimiento de animal
def guardar_descubrimiento(username, animal_id):
    usuarios = leer_usuarios()
    for usuario in usuarios:
        if usuario['username'] == username:
            descubrimientos = usuario['descubrimientos'].split(',') if usuario['descubrimientos'] else []
            if str(animal_id) not in descubrimientos:
                descubrimientos.append(str(animal_id))
                usuario['descubrimientos'] = ','.join(descubrimientos)
                break
    escribir_usuarios(usuarios)

# Función para obtener los descubrimientos de un usuario
def obtener_descubrimientos(username):
    usuarios = leer_usuarios()
    for usuario in usuarios:
        if usuario['username'] == username:
            return usuario['descubrimientos'].split(',') if usuario['descubrimientos'] else []
    return []
