from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.face_verification import load_image_with_opencv, verify_faces

router = APIRouter()

@router.post("/compare")
async def compare_faces_endpoint(known_image: UploadFile = File(...), compared_image: UploadFile = File(...)):
    if not known_image or not compared_image:
        raise HTTPException(status_code=400, detail="Missing image files")

    known_image_data = load_image_with_opencv(known_image.file)
    compared_image_data = load_image_with_opencv(compared_image.file)

    try:
        match = verify_faces(known_image_data, compared_image_data)
        return JSONResponse(content={"match": match})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
