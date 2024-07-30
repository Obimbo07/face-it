import cv2
import numpy as np
from deepface import DeepFace

def load_image_with_opencv(file):
    try:
        # Convert file to bytes and then to a NumPy array
        file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
        
        # Decode the image array
        image_array = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        
        # Check if the image was loaded successfully
        if image_array is None:
            raise ValueError("Unsupported image format or image could not be read")
        
        return image_array
    except Exception as e:
        raise ValueError(f"Unsupported image format: {e}")

def verify_faces(known_image, compared_image):
    # Perform face verification
    result = DeepFace.verify(known_image, compared_image)
    
    # Custom response formatting
    match_response = {
        "verified": result["verified"],
        "distance": result["distance"],
        "similarity_metric": result["similarity_metric"],
        "time": result.get("time", 0.0)
    }
    
    return {"match": match_response}
