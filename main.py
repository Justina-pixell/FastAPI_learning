from fastapi import FastAPI
from routes.health import health as health_router
from routes.status import status as patient_stat
from routes.info import information as patient_info

app=FastAPI()



app.include_router(health_router)
app.include_router(patient_stat)
app.include_router(patient_info)