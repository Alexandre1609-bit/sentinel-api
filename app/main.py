from fastapi import FastAPI
from app.config import settings

app = FastAPI()

@app.get("/status")
def read_status():
    #On utilise les variable chargées
    return {
        "status": "OK",
        "system": settings.app_name,
        "version": settings.app_version,
        "contact": settings.admin_email
    }