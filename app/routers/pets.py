from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.pet import Pet

router = APIRouter()


@router.get("/listarpets")
def listar_pets(db: Session = Depends(get_db)):
    pets = db.query(Pet).all()
    return pets


@router.get("/consultarpet/{pet_id}")
def consultar_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(Pet).filter(Pet.id == pet_id).first()

    if pet is None:
        raise HTTPException(status_code=404, detail="Pet não encontrado")

    return pet