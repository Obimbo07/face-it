import face_recognition


# def loading_images(file):
#   image_file = face_recognition.load_image_file(file)
#   image_encodings = face_recognition.face_encodings(image_file)[0]
  
#   if image_encodings == True:
#     print("Thank you we have your face encodings")
#   else:
#       print("Please upload your image again")
      
      
import face_recognition

def compare_faces(known_image_file, unknown_image_file):
    first_pic = face_recognition.load_image_file(known_image_file)
    known_face_encoding = face_recognition.face_encodings(first_pic)[0]
    
    second_pic = face_recognition.load_image_file(unknown_image_file)
    face_encoding_to_check = face_recognition.face_encodings(second_pic)[0]

    results = face_recognition.compare_faces([known_face_encoding], face_encoding_to_check)
    
    if results[0] == True:
        print("You have been successfully verified!")
        return True
    else:
        print("This is not you, please contact support")
        return False

