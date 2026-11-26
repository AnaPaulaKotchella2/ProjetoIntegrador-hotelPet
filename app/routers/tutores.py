from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.tutor import Tutor

router = APIRouter()


@router.get("/listartutores")
def listar_tutores(db: Session = Depends(get_db)):
    tutores = db.query(Tutor).all()
    return tutores


@router.get("/consultartutor/{tutor_id}")
def consultar_tutor(tutor_id: int, db: Session = Depends(get_db)):
    tutor = db.query(Tutor).filter(Tutor.id == tutor_id).first()

    if tutor is None:
        raise HTTPException(status_code=404, detail="Tutor não encontrado")

    return tutor