from fastapi import APIRouter
from pydantic import BaseModel
from app.services.recommender import recommend

router = APIRouter()

class Request(BaseModel):
    text: str

@router.post("/recommend")
def recommend_music(req: Request):
    return recommend(req.text)