# L'image de base
FROM python:3.10-slim

# Le dossier de travail
# # Exécuté en tant que Root pour les permissions d'écriture.
WORKDIR /code

# Installation des dépendances (En tant que Root!!!)
# Root a le droit d'écrire partout, donc pip install va marcher.
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copie du code (En tant que Root!)
COPY ./app /code/app/

# Création de l'utilisateur (Sécurité)
# On prépare l'identité du locataire.
RUN addgroup --system sentinelgroup && adduser --system --group sentineluser

# Transfert de propriété (Pour passer de Root à user)
# Maintenant que le dossier /code est rempli, Root donne les clés à SentinelUser.
# Si on ne fait pas ça, l'utilisateur ne pourra pas lire/exécuter le code.
RUN chown -R sentineluser:sentinelgroup /code

# Bascule (Sécurité)
# On ferme la porte. On devient l'utilisateur limité.
USER sentineluser

# Lancement
# C'est sentineluser qui lance la commande.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]