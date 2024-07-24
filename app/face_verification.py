import cv2
from deepface import DeepFace
import matplotlib.pyplot as plt
import numpy as np

def load_image_with_opencv(image_file):
    # Read the image file with OpenCV
    image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    # Convert BGR image (OpenCV default) to RGB (DeepFace default)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def verify_faces(known_image, compared_image):
    # Verify the faces using DeepFace with image arrays
    result = DeepFace.verify(img1_path=known_image, img2_path=compared_image)
    return result
