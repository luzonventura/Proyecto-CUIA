import cv2
import face_recognition
import time

# Imagen a comparar
image = cv2.imread("static/images/Reconocimiento.png")
face_locations = face_recognition.face_locations(image)

if face_locations:
    face_loc = face_locations[0]
    face_image_encodings = face_recognition.face_encodings(image, known_face_locations=[face_loc])[0]
else:
    print("No faces found in the image.")
    exit()

######################################################################################
# Video Streaming

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

start_time = None
admin_recognized = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image")
        break
    frame = cv2.flip(frame, 1)

    # Use the "hog" model for faster performance
    face_locations = face_recognition.face_locations(frame, model="hog")
    for face_location in face_locations:
        face_frame_encodings = face_recognition.face_encodings(frame, known_face_locations=[face_location])[0]
        result = face_recognition.compare_faces([face_image_encodings], face_frame_encodings)

        if result[0]:
            if start_time is None:
                start_time = time.time()
            elif time.time() - start_time >= 3:
                admin_recognized = True
                break
            text = "Admin"
            color = (125, 220, 0)
        else:
            start_time = None
            text = "Desconocido"
            color = (50, 50, 255)

        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.rectangle(frame, (left, bottom), (right, bottom + 30), color, cv2.FILLED)
        cv2.putText(frame, text, (left + 6, bottom + 24), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255), 1)

    cv2.imshow("Frame", frame)

    if admin_recognized:
        print("ACCESS_GRANTED")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
