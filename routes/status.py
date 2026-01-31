
from fastapi import APIRouter

status = APIRouter()

recovery_status = {
    1: {
        "patient_id": 1,
        "status": "improving",
        "notes": "Responding well to medication",
        "last_updated": "2026-01-30"
    },
    2: {
        "patient_id": 2,
        "status": "stable",
        "notes": "Iron levels improving",
        "last_updated": "2026-01-28"
    }
}
