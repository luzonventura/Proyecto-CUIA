import cv2
import cv2.aruco as aruco
import numpy as np
import pyttsx3
import speech_recognition as sr
import pandas as pd
from camara import cameraMatrix, distCoeffs
import threading
import time
import sys

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Configuración para la detección de ArUco
dictionaries = [
    aruco.getPredefinedDictionary(aruco.DICT_4X4_50),
    aruco.getPredefinedDictionary(aruco.DICT_6X6_50)
]

# Tamaño del marcador ArUco
marker_size = 0.05  # Ajusta según el tamaño de tus marcadores

# Cargar las imágenes para cada ID
images = {
    0: cv2.imread("static/images/Koala.png"),
    1: cv2.imread("static/images/Leon.png"),
    2: cv2.imread("static/images/Elefante.png"),
    3: cv2.imread("static/images/Pinguino.png"),
    4: cv2.imread("static/images/Buho.png"),
    5: cv2.imread("static/images/Murcielago.png")
}

# IDs de animales nocturnos
animales_nocturnos = [4, 5]

# Buffer para almacenar las detecciones recientes
detection_buffer = []
buffer_size = 10  # Ajusta el tamaño del buffer según sea necesario

# Cargar el CSV con la información de los animales
animal_data = pd.read_csv("animales.csv")

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

# Variables de control
recognition_in_progress = False
current_animal_id = None
lock = threading.Lock()
stop_event = threading.Event()

# Función para aplicar el filtro nocturno
def aplicar_filtro_nocturno(frame):
    filtro_nocturno = np.zeros_like(frame)
    filtro_nocturno[:, :] = (100, 0, 0)
    frame = cv2.addWeighted(frame, 0.5, filtro_nocturno, 0.5, 0)
    return frame

# Función para procesar y superponer la imagen correspondiente al ID
def process_and_overlay_image(frame, dictionary):
    global current_animal_id, recognition_in_progress, stop_event
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = aruco.detectMarkers(gray, dictionary)

    if ids is not None:
        rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(corners, marker_size, cameraMatrix, distCoeffs)

        for rvec, tvec, corner, aruco_id in zip(rvecs, tvecs, corners, ids):
            aruco_id = aruco_id[0]
            if 0 <= aruco_id <= 5:
                detection_buffer.append(aruco_id)
                if len(detection_buffer) > buffer_size:
                    detection_buffer.pop(0)

                most_common_id = max(set(detection_buffer), key=detection_buffer.count)

                if most_common_id != current_animal_id:
                    with lock:
                        current_animal_id = most_common_id
                        print(f"DESCUBIERTO: {current_animal_id}")

                    if recognition_in_progress:
                        stop_event.set()
                        recognition_in_progress = False

                    stop_event.clear()
                    recognition_thread = threading.Thread(target=provide_animal_info)
                    recognition_thread.start()

                if current_animal_id in animales_nocturnos:
                    frame = aplicar_filtro_nocturno(frame)

                image_to_overlay = images.get(current_animal_id, None)
                if image_to_overlay is not None:
                    overlay_height, overlay_width, _ = image_to_overlay.shape
                    corners_2d = np.float32(corner).reshape(-1, 2)
                    original_points = np.array([
                        [0, 0],
                        [overlay_width, 0],
                        [overlay_width, overlay_height],
                        [0, overlay_height]
                    ], dtype=np.float32)
                    transformation_matrix = cv2.getPerspectiveTransform(original_points, corners_2d)
                    overlay = cv2.warpPerspective(image_to_overlay, transformation_matrix, (frame.shape[1], frame.shape[0]))
                    mask = cv2.cvtColor(overlay, cv2.COLOR_BGR2GRAY)
                    _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY_INV)
                    frame = cv2.bitwise_and(frame, frame, mask=mask)
                    frame = cv2.bitwise_or(frame, overlay)

    return frame

def provide_animal_info():
    global recognition_in_progress, stop_event
    recognition_in_progress = True

    with lock:
        animal_id = current_animal_id

    recognizer = sr.Recognizer()

    while not stop_event.is_set():
        with sr.Microphone() as source:
            print("Diga 'Descripción', 'Hábitat' o 'Dieta' para obtener información sobre el animal.")
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio, language='es-ES').lower()
                with lock:
                    if animal_id != current_animal_id:
                        recognition_in_progress = False
                        return  # Si el animal_id ha cambiado, salir de la función

                if 'descripción' in command or 'descripcion' in command:
                    engine.say(animal_data.loc[animal_data['marker_id'] == animal_id, 'descripcion'].values[0])
                elif 'hábitat' in command or 'habitat' in command:
                    engine.say(animal_data.loc[animal_data['marker_id'] == animal_id, 'habitat'].values[0])
                elif 'dieta' in command:
                    engine.say(animal_data.loc[animal_data['marker_id'] == animal_id, 'dieta'].values[0])
                elif 'salir' in command:
                    engine.say("Saliendo del safari.")
                    engine.runAndWait()
                    release_resources()
                    sys.exit(0)
                engine.runAndWait()

                # Espera 2 segundos y vuelve a solicitar un comando
                time.sleep(1)
            
            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass

    recognition_in_progress = False

def release_resources():
    cap.release()
    cv2.destroyAllWindows()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    for dictionary in dictionaries:
        frame = process_and_overlay_image(frame, dictionary)

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        stop_event.set()
        recognition_in_progress = False
        release_resources()
        break
    
release_resources()
