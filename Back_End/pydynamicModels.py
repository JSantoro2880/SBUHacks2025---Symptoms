from pydantic import BaseModel

class SymptomEntryCreate(BaseModel):
    symptoms_text: str

class DiagnosisRead(BaseModel):
    id: int
    symptom_entry_id: int
    diagnosis_text: str

    class Config:
        orm_mode = True

class SymptomEntryRead(BaseModel):
    id: int
    symptoms_text: str
    diagnosis: DiagnosisRead | None = None

    class Config:
        orm_mode = True