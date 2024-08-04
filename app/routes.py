from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.face_recognition import  compare_faces

router = APIRouter()

@router.post("/compare")
async def compare_faces_endpoint(known_image: UploadFile = File(...), compared_image: UploadFile = File(...)):
    if not known_image or not compared_image:
        raise HTTPException(status_code=400, detail="Missing image files")

    known_image_data = known_image.file
    compared_image_data = compared_image.file

    try:
        return JSONResponse(content={"status": "This endpoint is under development! Please contact support for assistance"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.post("/verify_attendance")
async def face_comparison(first_image_attendance: UploadFile = File(...), second_image_attendance: UploadFile = File(...)):
    if not first_image_attendance or not second_image_attendance:
        raise HTTPException(status_code=400, detail="Missing image files")

    try:
        # first_image_attendance_data = await first_image_attendance.read()
        # second_image_attendance_data = await second_image_attendance.read()
        
        # firstimage_attendance = loading_images(first_image_attendance_data)
        # secondimage_attendance = loading_images(second_image_attendance_data)
        
        matching = compare_faces(first_image_attendance.file, second_image_attendance.file)
        return JSONResponse(content={"matching": matching})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))