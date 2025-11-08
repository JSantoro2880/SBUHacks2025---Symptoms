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
    entry_symptoms = relationship("EntrySymptom", back_populates="user")  


class Diagnosis(Base):
    __tablename__ = "diagnoses"
    id = Column(Integer, primary_key=True)
    symptom_entry_id = Column(Integer, ForeignKey("symptom_entries.id"), unique=True, nullable=False)
    diagnosis_text = Column(Text, nullable=False)

    symptom_entry = relationship("SymptomEntry", back_populates="diagnosis")


class SymptomCategory(Base):
    __tablename__ = "symptom_categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    symptoms = relationship("Symptom", back_populates="category")


class Symptom(Base):
    __tablename__ = "symptoms"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    category_id = Column(Integer, ForeignKey("symptom_categories.id"), nullable=False)

    category = relationship("SymptomCategory", back_populates="symptoms")


class SymptomEntry(Base):
    __tablename__ = "symptom_entries"
    id = Column(Integer, primary_key=True)
    submitted_at = Column(DateTime(timezone=True), server_default=func.now())

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  
    user = relationship("User", back_populates="symptom_entries")    

    entry_symptoms = relationship("EntrySymptom", back_populates="symptom_entry")
    diagnosis = relationship("Diagnosis", back_populates="symptom_entry", uselist=False)


class EntrySymptom(Base):
    __tablename__ = "entry_symptoms"
    id = Column(Integer, primary_key=True)
    symptom_entry_id = Column(Integer, ForeignKey("symptom_entries.id"), nullable=False)
    symptom_id = Column(Integer, ForeignKey("symptoms.id"), nullable=True)
    custom_symptom = Column(String(255), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    symptom_entry = relationship("SymptomEntry", back_populates="entry_symptoms")
    symptom = relationship("Symptom")
    user = relationship("User", back_populates="entry_symptoms")
