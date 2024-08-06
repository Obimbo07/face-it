from  fastapi import HTTPException
from  fastapi.responses import JSONResponse

# def loading_images(file):
#   image_file = face_recognition.load_image_file(file)
#   image_encodings = face_recognition.face_encodings(image_file)[0]
  
#   if image_encodings == True:
#     print("Thank you we have your face encodings")
#   else:
#       print("Please upload your image again")
      
      
import face_recognition

def compare_faces(known_image_file, unknown_image_file):
    try:
        first_pic = face_recognition.load_image_file(known_image_file)
        known_face_encoding = face_recognition.face_encodings(first_pic)[0]
        
        second_pic = face_recognition.load_image_file(unknown_image_file)
        face_encoding_to_check = face_recognition.face_encodings(second_pic)[0]

        compare_results = face_recognition.compare_faces([known_face_encoding], face_encoding_to_check, tolerance=0.2)
        compare_distance = face_recognition.face_distance([known_face_encoding], face_encoding_to_check)
        
        results = bool(compare_results[0])
        distance = float(compare_distance)

        return { "match": results, "distance": distance }
    except IndexError:
       raise HTTPException(status_code=400, detail="No face found on both Images. Please take a potrait with your face straight")
