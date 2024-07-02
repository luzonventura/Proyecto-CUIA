# Proyecto Safari Virtual

¡Bienvenido al repositorio del Proyecto Safari Virtual! Este archivo README proporciona una visión general del proyecto, sus objetivos, funcionalidades, estructura, dependencias y manual de usuario.

## Descripción del Proyecto
El Safari Virtual es una aplicación educativa diseñada para proporcionar a los usuarios una experiencia interactiva de descubrimiento de animales mediante el uso de tecnología de reconocimiento visual y de voz. Utilizando marcadores ArUco y reconocimiento facial, los usuarios pueden explorar y aprender sobre diferentes animales de manera divertida y educativa. El sistema está pensado para ser utilizado por niños, estudiantes y cualquier persona interesada en la fauna.

## Objetivos del Proyecto
- **Educación Interactiva**: Proveer una plataforma interactiva para el aprendizaje sobre animales, sus hábitats, dietas y características.
- **Uso de Tecnología Innovadora**: Implementar tecnologías como reconocimiento facial y detección de marcadores ArUco para mejorar la experiencia del usuario.
- **Gestión de Usuarios y Descubrimientos**: Permitir a los usuarios gestionar sus cuentas y descubrimientos, y proporcionar a los administradores herramientas para la gestión de usuarios.

## Funcionalidades Principales

### Inicio de Sesión y Registro
- **Inicio de Sesión**: Los usuarios pueden iniciar sesión utilizando su nombre de usuario y contraseña.
- **Registro de Nuevos Usuarios**: Los nuevos usuarios pueden registrarse proporcionando su nombre, apellido, correo electrónico, nombre de usuario y contraseña.
- **Acceso por Reconocimiento Facial**: El administrador puede acceder al sistema mediante reconocimiento facial, proporcionando una capa adicional de seguridad y conveniencia.

### Descubrimiento de Animales
- **Detección de Marcadores ArUco**: Utiliza la cámara del dispositivo para detectar marcadores ArUco que representan diferentes animales.
- **Superposición de Imágenes**: Cuando se detecta un marcador, la imagen correspondiente del animal se superpone en la vista de la cámara.
- **Interacción de Voz**: Los usuarios pueden interactuar con el sistema mediante comandos de voz para obtener información sobre los animales descubiertos.

### Gestión de Usuarios y Descubrimientos
- **Vista de Descubrimientos**: Los usuarios pueden ver una galería de los animales que han descubierto.
- **Gestión de Usuarios (Admin)**: El administrador puede gestionar las cuentas de los usuarios, incluyendo la eliminación de usuarios y descubrimientos.
- **Registro de Descubrimientos**: Cada descubrimiento de un usuario se guarda y puede ser revisado posteriormente.

### Tutorial
- **Guía Interactiva**: Proporciona un tutorial que explica cómo utilizar la aplicación, incluyendo cómo iniciar el safari, escanear marcadores y explorar los animales descubiertos.

## Estructura del Proyecto

### Backend (Flask)
El backend de la aplicación está desarrollado utilizando el framework Flask. Se encarga de gestionar las solicitudes HTTP, interactuar con la base de datos y manejar la lógica de la aplicación.

- `app.py`: Contiene las rutas y la lógica principal del servidor Flask.
- `user_management.py`: Maneja la lógica relacionada con la gestión de usuarios, incluyendo el registro, inicio de sesión y descubrimientos.
- `face_recognition_login.py`: Script para manejar el inicio de sesión por reconocimiento facial.
- `safarivirtual.py`: Script para la detección de marcadores ArUco y la interacción de voz.
- `animales.csv`: Archivo CSV que contiene información sobre los animales.
- `usuarios.csv`: Archivo CSV que contiene información sobre los usuarios.

### Frontend (Templates y Estilos)
El frontend de la aplicación consiste en plantillas HTML, hojas de estilo CSS y scripts JavaScript.

- `templates/`: Contiene las plantillas HTML para las diferentes páginas de la aplicación.
  - `index.html`: Página de inicio de sesión.
  - `register.html`: Página de registro de usuarios.
  - `main.html`: Página principal donde se muestran los descubrimientos del usuario.
  - `animal.html`: Página que muestra información detallada sobre un animal específico.
  - `manage_users.html`: Página de gestión de usuarios para el administrador.
  - `tutorial.html`: Página que proporciona un tutorial interactivo sobre cómo usar la aplicación.
- `static/css/style.css`: Archivo de estilos CSS para la aplicación.
- `static/images/`: Contiene las imágenes de los animales y otros elementos gráficos.
- `static/js/script.js`: Contiene scripts JavaScript necesarios para la funcionalidad interactiva de la aplicación.

## Dependencias
La aplicación depende de varios paquetes de Python, que se enumeran en el archivo `requirements.txt`. A continuación, se muestra una lista de las dependencias principales:

- Flask: Framework web para Python.
- pandas: Biblioteca para la manipulación y análisis de datos.
- opencv-python: Herramientas para el procesamiento de imágenes y visión por computadora.
- face_recognition: Biblioteca para el reconocimiento facial.
- pyttsx3: Motor de texto a voz.
- SpeechRecognition: Biblioteca para el reconocimiento de voz.
- numpy: Biblioteca para el cálculo numérico.

## Manual de usuario

### Inicio de Sesión
Pasos para Iniciar Sesión:

1. Abre la aplicación en tu navegador web.
2. En la página de inicio, ingresa tu nombre de usuario y contraseña en los campos correspondientes.
3. Haz clic en el botón "Acceder".

**Acceso por Reconocimiento Facial**:

1. En la página de inicio, haz clic en el botón "Acceder por cámara".
2. La cámara se activará y tratará de reconocer tu rostro. Asegúrate de estar bien iluminado y centrado en la cámara.
3. Si el reconocimiento facial tiene éxito, serás redirigido a la página principal.

**Registro de Nuevos Usuarios**:

1. En la página de inicio, haz clic en el enlace "Regístrate aquí".
2. Completa el formulario de registro con tu nombre, apellido, correo electrónico, nombre de usuario y contraseña.
3. Haz clic en el botón "Registrar".
4. Si el registro es exitoso, serás redirigido a la página de inicio para iniciar sesión.

### Página Principal
**Bienvenida**:
- Al iniciar sesión, serás recibido con un mensaje de bienvenida personalizado.
- Si eres el administrador, tu nombre aparecerá con un estilo destacado.

**Visualización de Animales Descubiertos**:
- En la página principal, podrás ver una galería de los animales que has descubierto.
- Haz clic en cualquier imagen de animal para ver información detallada sobre él.

**Iniciar Safari**:

1. Desde la página principal, haz clic en el botón "Entrar al safari".
2. La cámara de tu dispositivo se activará y podrás comenzar a escanear los marcadores ArUco para descubrir animales.

**Tutorial**:
- Si eres nuevo en la aplicación o necesitas ayuda, haz clic en el botón "Ir al Tutorial" para obtener una guía detallada sobre cómo utilizar la aplicación.

**Cerrar Sesión**:
- Para cerrar sesión, haz clic en el botón "Cerrar sesión".

### Gestión de Usuarios (Solo Administrador)
- Si eres administrador, tendrás la opción adicional de "Gestionar Usuarios". Haz clic en este botón para acceder a la página de gestión de usuarios.

### Descubrimiento de Animales
**Escaneo de Marcadores ArUco**:

1. Asegúrate de tener los marcadores ArUco impresos y listos para escanear.
2. Dirige la cámara de tu dispositivo hacia el marcador ArUco.
3. La aplicación detectará el marcador y superpondrá la imagen del animal correspondiente en la vista de la cámara.

**Interacción de Voz**:

1. Cuando descubras un animal, la aplicación te preguntará si deseas saber más sobre él.
2. Responde utilizando tu voz. Puedes preguntar sobre la descripción, hábitat o dieta del animal.
3. La aplicación proporcionará la información solicitada utilizando texto a voz.

### Información del Animal
**Visualización de Detalles**:
- Al hacer clic en la imagen de un animal en la página principal, serás redirigido a una página que muestra detalles específicos sobre el animal.
- La página de detalles incluye información sobre la descripción, hábitat y dieta del animal.
- También se muestra una imagen del animal.

**Navegación**:
- Para regresar a la página principal desde la página de detalles del animal, haz clic en el botón "Volver al perfil".

### Gestión de Usuarios (Solo Administrador)
**Visualización de Usuarios**:
- En la página de gestión de usuarios, se muestra una tabla con todos los usuarios registrados, junto con su nombre, apellido, correo electrónico y descubrimientos.

**Eliminar Usuarios**:

1. En la tabla de usuarios, identifica al usuario que deseas eliminar.
2. Haz clic en el botón "Eliminar" correspondiente al usuario.
3. El usuario será eliminado del sistema.

**Eliminar Descubrimientos**:

1. Arrastra la imagen del descubrimiento de la tabla de usuarios hacia la zona de eliminación.
2. El descubrimiento será eliminado de la cuenta del usuario.

**Navegación**:
- Para regresar a la página principal desde la página de gestión de usuarios, haz clic en el botón "Volver a la Página Principal".

### Tutorial
**Acceso al Tutorial**:
- Desde la página principal, haz clic en el botón "Ir al Tutorial".

**Contenido del Tutorial**:
- El tutorial proporciona una guía paso a paso sobre cómo utilizar la aplicación:
  - **Ejecutar el Programa**: Cómo iniciar el safari y activar la cámara.
  - **Escanear Marcadores ArUco**: Consejos sobre cómo escanear los marcadores para descubrir animales.
  - **Descubrir y Aprender**: Cómo interactuar con los animales descubiertos y obtener información sobre ellos.
  - **Guardar tus Descubrimientos**: Cómo se guardan y muestran los descubrimientos en tu perfil.

## Resolución de Problemas Comunes
**Problemas con el Inicio de Sesión**:
- Asegúrate de que tu nombre de usuario y contraseña sean correctos.
- Si olvidaste tu contraseña, contacta al administrador para restablecerla.

**Problemas con el Reconocimiento Facial**:
- Asegúrate de estar bien iluminado y centrado en la cámara.
- Si el reconocimiento facial falla repetidamente, intenta iniciar sesión con tu nombre de usuario y contraseña.

**Problemas con la Detección de Marcadores ArUco**:
- Asegúrate de que los marcadores estén impresos claramente y no estén dañados.
- Escanea los marcadores en un entorno bien iluminado.

**Problemas con la Interacción de Voz**:
- Asegúrate de que el micrófono esté funcionando y configurado correctamente.
- Habla claramente y con un volumen adecuado.
- Intenta usar frases sencillas y específicas como "descripción", "hábitat" o "dieta".
