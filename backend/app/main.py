from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app import models, database
from app.models import Thought
from app.database import get_db
from pydantic import BaseModel
from typing import List
import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ThoughtCreate(BaseModel):
    text: str

class ThoughtResponse(BaseModel):
    id: int
    text: str
    timestamp: datetime.datetime

    class Config:
        orm_mode = True

@app.get("/thoughts", response_model=List[ThoughtResponse])
def get_thoughts(db: Session = Depends(get_db)):
    return db.query(Thought).order_by(Thought.timestamp).all()

@app.post("/thoughts", response_model=ThoughtResponse)
def create_thought(thought: ThoughtCreate, db: Session = Depends(get_db)):
    new_thought = Thought(text=thought.text, timestamp=datetime.datetime.now())
    db.add(new_thought)
    db.commit()
    db.refresh(new_thought)
    return new_thought
