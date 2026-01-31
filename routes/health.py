# adding health data for a patient

# retrieving health data

# updating health records

# Examples of what belongs here:

# blood pressure

# heart rate

# diagnosis summary

# allergies

# chronic conditions

from fastapi import APIRouter

health = APIRouter()

health_records = {
    1: {
        "patient_id": 1,
        "blood_pressure": "120/80",
        "heart_rate": 72,
        "allergies": ["penicillin"],
        "diagnosis": "mild hypertension"
    },
    2: {
        "patient_id": 2,
        "blood_pressure": "110/70",
        "heart_rate": 68,
        "allergies": [],
        "diagnosis": "anemia"
    }
}


