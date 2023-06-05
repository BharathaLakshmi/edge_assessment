from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import edge
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status, APIRouter, Response
from app.database import get_db, engine
import app.models as models
import app.schemas as schemas
app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(edge.router, tags=['Add_data'], prefix='/add_data')
app.include_router(edge.router, tags=['Update_data'], prefix='/update_data')
db = Session(engine)

@app.get('/api/healthchecker')
def root():
    return {'message': 'Hello World'}

@app.get('/get_data')
def _get_data(source_id: int, response: Response):

    post = db.query(models.Source).filter(models.Source.source_id == source_id).first()
    return post

@app.get('/get_data_trigger')
def _get_data_trigger(source_id: int, response: Response):

    post = db.query(models.Source).filter(models.Source.source_id == source_id).first()
    final_from_date = post.from_date + timedelta(minutes=int(post.frequency.split("M")[0]))
    final_to_date = post.to_date + timedelta(minutes=int(post.frequency.split("M")[0]))
    updated_dict = {
        "source_id": post.source_id,
        "source": post.source,
        "source_type":post.source_type, 
        "source_tag":post.source_tag, 
        "from_date": final_from_date, 
        "to_date": final_to_date, 
        "frequency": post.frequency}
    return updated_dict

