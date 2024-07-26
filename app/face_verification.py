# face_verification.py
import cv2
import numpy as np
from deepface import DeepFace

def load_image_with_opencv(file):
    # Read image file
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    return image

def verify_faces(known_image, compared_image):
    # Perform face verification
    result = DeepFace.verify(known_image, compared_image)
    return result["verified"]
