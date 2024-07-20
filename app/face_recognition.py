import cv2
import face_recognition
import numpy as np

def load_image_with_opencv(image_file):
    # Read the image file with OpenCV
    image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    # Convert BGR image (OpenCV default) to RGB (face_recognition default)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def encode_face(image):
    # Get face encodings
    face_encodings = face_recognition.face_encodings(image)
    if face_encodings:
        return face_encodings[0]  # Return the encoding of the first face
    return None

def compare_faces(known_encodings, face_to_compare_encoding):
    # Compare faces and get the distance
    return face_recognition.compare_faces(known_encodings, face_to_compare_encoding, tolerance=0.6), face_recognition.face_distance(known_encodings, face_to_compare_encoding)
