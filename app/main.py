from fastapi import FastAPI
from typing import Dict # On importe le type "Dictionnaire"

app = FastAPI()

@app.get("/status")
def read_status() -> Dict[str, str]:
    """
    Vérifie l'état de santé de l'API.
    Retourne un JSON indiquant si le système est opérationnel.
    """
    return {"status": "OK", "system": "Sentinel-API Ready"}