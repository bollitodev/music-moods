import uuid

from fastapi import APIRouter, File, UploadFile

from app.models import Recommendation
from app.services.fer_model import FacialExpressionRecognitionModel as FERModel
from app.services.song_recommendation import SongRecommendation

router = APIRouter()
fer_model = FERModel()
song_recommendation = SongRecommendation()

@router.post("/recommendations/", tags=["recommendations"], response_model=Recommendation)
async def read_recommendations(face_picture: UploadFile = File(...)) -> Recommendation:
    face_picture.filename = f"{uuid.uuid4()}.jpg"
    contents = await face_picture.read()
    emotion = fer_model.predict(contents)
    recomendation = song_recommendation.recommend(emotion)

    return recomendation   