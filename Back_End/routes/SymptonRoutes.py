from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
import models, pydynamicModels
from database import engine, Base, getDB

router = APIRouter()

@router.post("/add/symptoms")
def submitSolutions(symptom : pydynamicModels.SymptomEntryCreate, db : Session = Depends(getDB)):

    ##add user id when we make login
    symptom_entry = models.SymptomEntry(symptoms_text=symptom.symptoms_text)
    db.add(symptom_entry)
    db.commit()
    db.refresh(symptom_entry)

    #MAKE CALL HERE TO GET DIAGNOSIS, THIS IS JUST TESITNG ROUTE
    diagnosis_text = "This is a dummy diagnosis based on symptoms."
    diagnosis = models.Diagnosis(symptom_entry_id=symptom_entry.id, diagnosis_text=diagnosis_text)
    db.add(diagnosis)
    db.commit()
    db.refresh(diagnosis)

    return symptom_entry


@router.get("/symptoms/{id}")
def getSymptomEntry(id: int, db: Session = Depends(getDB)):
    symptom_entry = db.query(models.SymptomEntry).filter(models.SymptomEntry.id == id).first()
    if not symptom_entry:
        raise HTTPException(status_code=404, detail="Symptom entry not found")
    return symptom_entry