# Safari Virtual: Descubrimiento de Animales con Realidad Aumentada

Safari Virtual es una aplicación web basada en Flask que utiliza realidad aumentada y reconocimiento de voz para proporcionar una experiencia interactiva de descubrimiento de animales. Detecta marcadores ArUco a través de una cámara y superpone imágenes e información sobre los animales detectados.

## Características

- Detección en tiempo real de marcadores ArUco
- Superposición de imágenes de animales en los marcadores con realidad aumentada
- Funcionalidad de comandos de voz para obtener información sobre los animales
- Inicio de sesión y registro de usuarios
- Gestión de usuarios y descubrimientos (solo para administradores)
- Guía interactiva de usuario

## Requisitos

- Python 3.7+
- Flask
- pandas
- OpenCV (opencv-python)
- face_recognition
- pyttsx3
- SpeechRecognition
- numpy

### Instalación de dependencias

Para instalar las dependencias, utiliza el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Uso

1. Ejecuta app.py
2. Abre un navegador web y navega a `http://localhost:5000`.

3. Usa el menú de navegación para acceder a las diferentes características:

- Inicio: Página principal
- Registro: Página de registro de usuarios
- Cámara: Vista de realidad aumentada
- Descubrimientos: Lista de animales descubiertos
- Gestión de Usuarios: Gestión de cuentas de usuario (solo para administradores)
- Tutorial: Guía interactiva de usuario

4. En la vista de Cámara, apunta la cámara a los marcadores ArUco para ver las imágenes de los animales y la información correspondiente.

5. Usa comandos de voz para obtener información sobre los animales:

- "descripción": Muestra la descripción del animal en pantalla
- "hábitat": Muestra el hábitat del animal en pantalla
- "dieta": Muestra la dieta del animal en pantalla
- "salir": Para salir del safari virtual

## Estructura del Proyecto

- `app.py`: Aplicación principal de Flask
- `user_management.py`: Gestión de usuarios, registro e inicio de sesión
- `face_recognition_login.py`: Inicio de sesión por reconocimiento facial
- `safarivirtual.py`: Detección de marcadores ArUco e interacción de voz
- `animales.csv`: Base de datos de información sobre los animales
- `usuarios.csv`: Base de datos de información sobre los usuarios
- `templates/`: Plantillas HTML para las páginas web
  - `index.html`: Página de inicio de sesión
  - `register.html`: Página de registro de usuarios
  - `main.html`: Página principal con los descubrimientos del usuario
  - `animal.html`: Página con información detallada sobre un animal
  - `manage_users.html`: Página de gestión de usuarios para el administrador
  - `tutorial.html`: Página con la guía interactiva
- `static/css/style.css`: Estilos CSS
- `static/js/script.js`: Scripts JavaScript
- `static/images/`: Imágenes de los animales y elementos gráficos
