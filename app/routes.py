from flask import Blueprint, request, jsonify
from app.face_verification import load_image_with_opencv, verify_faces

main = Blueprint('main', __name__)

@main.route('/compare', methods=['POST'])
def compare_faces_endpoint():
    known_image = request.files.get('known_image')
    compared_image = request.files.get('compared_image')

    if not known_image or not compared_image:
        return jsonify({"error": "Missing image files"}), 400

    # Load images with OpenCV
    known_image_data = load_image_with_opencv(known_image)
    compared_image_data = load_image_with_opencv(compared_image)

    try:
        # Verify faces using DeepFace with image arrays
        match = verify_faces(known_image_data, compared_image_data)
        return(match)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
