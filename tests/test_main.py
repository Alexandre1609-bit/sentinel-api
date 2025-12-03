from fastapi.testclient import TestClient
from app.main import app
from app.config import settings

#On crée le simulateur
client = TestClient(app)


#Si la fonction ne commence pas par 'test_', pytest va l'ignorer. (Convention obligatoire)
def test_read_status_return_200():
    """
    Vérifie que l'endpoint '/status' est accessible et renvoie un correctement.
    """
    #Action (GIVEN / WHEN)
    #Le client envoie une requête GET virtuelle à l'application
    response = client.get("/status")

    #Vérification (THEN)
    #On vérifie que le serveur n'a pas planté (Rappel : code 200 = OK)
    assert response.status_code == 200 #Si le code = 200, le code continue, sinon (500, 404...) le code s'arrête.

    except_json = {
        "status": "OK",
        "system": settings.app_name,
        "version": settings.app_version,
        "contact": settings.admin_email
    }
    assert response.json() == except_json