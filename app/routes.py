from flask import Blueprint, request, jsonify
from app.face_recognition import load_image_with_opencv, encode_face, compare_faces

main = Blueprint('main', __name__)

@main.route('/compare', methods=['POST'])
def compare_faces_endpoint():
    known_image = request.files.get('known_image')
    compared_image = request.files.get('compared_image')

    if not known_image or not compared_image:
        return jsonify({"error": "Missing image files"}), 400

    # Load and process images
    known_image_data = load_image_with_opencv(known_image)
    compared_image_data = load_image_with_opencv(compared_image)

    # Encode faces
    known_encoding = encode_face(known_image_data)
    compared_encoding = encode_face(compared_image_data)

    if known_encoding is None or compared_encoding is None:
        return jsonify({"error": "Failed to encode one or both images"}), 400

    # Compare faces
    match_results, distance = compare_faces([known_encoding], compared_encoding)
    
    # Convert numpy types to native Python types
    match_results = [bool(result) for result in match_results]
    distance = [float(d) for d in distance]

    return jsonify({
        "match": match_results[0],
        "distance": distance[0]  # Convert numpy.float32 to Python float
    })
