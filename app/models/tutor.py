from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Tutor(Base):
    __tablename__ = "tutores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    telefone = Column(String(20))
    cpf = Column(String(14))
    email = Column(String(100))
    nascimento = Column(String(20))

    pets = relationship("Pet", back_populates="tutor")