from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=True)
    hashed_password = Column(String(255), nullable=True) 
    
    symptom_entries = relationship("SymptomEntry", back_populates="user")

class SymptomEntry(Base):
    __tablename__ = "symptom_entries"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  
    symptoms_text = Column(Text, nullable=False)  
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User", back_populates="symptom_entries")
    diagnosis = relationship("Diagnosis", back_populates="symptom_entry", uselist=False)

class Diagnosis(Base):
    __tablename__ = "diagnoses"
    
    id = Column(Integer, primary_key=True, index=True)
    symptom_entry_id = Column(Integer, ForeignKey("symptom_entries.id"), unique=True, nullable=False)
    diagnosis_text = Column(Text, nullable=False)  
    confidence_score = Column(String(20), nullable=True)  
    
    symptom_entry = relationship("SymptomEntry", back_populates="diagnosis")
