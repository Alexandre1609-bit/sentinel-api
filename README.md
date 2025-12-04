
# Sentinel-API

Sentinel-API est une API REST minimaliste conçue comme un laboratoire d'apprentissage autour des pratiques DevOps, du Clean Code et des standards de développement modernes.

## Contexte et objectifs

Ce projet a été réalisé en autodidacte dans le cadre de ma préparation au BUT Informatique.
L'objectif n'est pas seulement de créer une API fonctionnelle, mais d'adopter dès le départ des bonnes pratiques professionnelles : structure propre, sécurité, conteneurisation et qualité du code.

### Compétences visées

- **Architecture logicielle** : Organisation claire et séparation des responsabilités.
- **Conteneurisation** : Images Docker optimisées, principe du moindre privilège.
- **Qualité du code** : Typage strict, documentation automatique, gestion structurée des dépendances.
- **Sécurité (approche "Shift Left")** : Audit de vulnérabilités avec pip-audit, exécution en utilisateur non-root.

## Stack technique

- Python 3.10
- FastAPI
- Uvicorn (ASGI)
- Docker / Docker Desktop
- pip-audit

## Installation et démarrage

### Prérequis

- Docker Desktop
- Git

### 1. Lancement avec Docker (méthode recommandée)

```bash
git clone [https://github.com/Alexandre1609-bit/sentinel-api.git](https://github.com/Alexandre1609-bit/sentinel-api.git)
cd sentinel-api

docker build -t sentinel-api .
docker run -d -p 8000:80 --name sentinel-container sentinel-api
```

L'API sera accessible sur : http://localhost:8000

### 2. Développement local

Créer un environnement virtuel :

```
python -m venv venv

Windows :
.\venv\Scripts\activate

Linux/macOS :
source venv/bin/activate

Installer les dépendances :
pip install -r requirements.txt

Lancer le serveur FastAPI :
uvicorn app.main:app --reload
```
## Sécurité et architecture

Le projet applique plusieurs bonnes pratiques :

- Exécution en utilisateur non-root dans le conteneur (sentineluser).
- Dépendances figées dans requirements.txt pour assurer la reproductibilité.
- Utilisation d'un environnement virtuel en local.
- Audit de vulnérabilités via pip-audit.

## Documentation API

Une documentation interactive (Swagger UI) est disponible à l'adresse suivante : http://localhost:8000/docs

## Auteur

Alexandre étudiant autodidacte.


## Avertissement et statut du projet

Ce projet n’a pas vocation à être utilisé en production. Il s’agit principalement d’un terrain d’expérimentation pour apprendre à structurer un projet, comprendre Docker et découvrir FastAPI. Je l’utilise comme support pour progresser en autonomie.

Ce projet n’est pas :

- Une API destinée à la production
- Un framework
- Un projet finalisé
- C’est avant tout un support d’apprentissage.

## Ressources et méthode

Ressources utilisées (mises à jour régulièrement) :

- Documentation FastAPI
- Documentation Docker
- Tutoriels open-source / vidéos pédagogiques

Note sur l'IA :  L’IA est utilisée uniquement lorsque je ne parviens pas à trouver la solution par moi-même, afin de privilégier la recherche et la compréhension. 
Aucune génération de code n'est effectuée; l'écriture et l'implémentation sont entièrement manuelles pour garantir une maîtrise complète du projet.

=======
# Sentinel-API

Sentinel-API est une API REST minimaliste conçue comme un laboratoire d'apprentissage autour des pratiques DevOps, du Clean Code et des standards de développement modernes.

## Contexte et objectifs

Ce projet a été réalisé en autodidacte dans le cadre de ma préparation au BUT Informatique.
L'objectif n'est pas seulement de créer une API fonctionnelle, mais d'adopter dès le départ des bonnes pratiques professionnelles : structure propre, sécurité, conteneurisation et qualité du code.

### Compétences visées

- **Architecture logicielle** : Organisation claire et séparation des responsabilités.
- **Conteneurisation** : Images Docker optimisées, principe du moindre privilège.
- **Qualité du code** : Typage strict, documentation automatique, gestion structurée des dépendances.
- **Sécurité (approche "Shift Left")** : Audit de vulnérabilités avec pip-audit, exécution en utilisateur non-root.

## Stack technique

- Python 3.10
- FastAPI
- Uvicorn (ASGI)
- Docker / Docker Desktop
- pip-audit

## Installation et démarrage

### Prérequis

- Docker Desktop
- Git

### 1. Lancement avec Docker (méthode recommandée)

```bash
git clone [https://github.com/Alexandre1609-bit/sentinel-api.git](https://github.com/Alexandre1609-bit/sentinel-api.git)
cd sentinel-api

docker build -t sentinel-api .
docker run -d -p 8000:80 --name sentinel-container sentinel-api
```

L'API sera accessible sur : http://localhost:8000

### 2. Développement local

Créer un environnement virtuel :

```
python -m venv venv

Windows :
.\venv\Scripts\activate

Linux/macOS :
source venv/bin/activate

Installer les dépendances :
pip install -r requirements.txt

Lancer le serveur FastAPI :
uvicorn app.main:app --reload
```
## Sécurité et architecture

Le projet applique plusieurs bonnes pratiques :

- Exécution en utilisateur non-root dans le conteneur (sentineluser).
- Dépendances figées dans requirements.txt pour assurer la reproductibilité.
- Utilisation d'un environnement virtuel en local.
- Audit de vulnérabilités via pip-audit.

## Documentation API

Une documentation interactive (Swagger UI) est disponible à l'adresse suivante : http://localhost:8000/docs

## Auteur

Alexandre étudiant autodidacte.


## Avertissement et statut du projet

Ce projet n’a pas vocation à être utilisé en production. Il s’agit principalement d’un terrain d’expérimentation pour apprendre à structurer un projet, comprendre Docker et découvrir FastAPI. Je l’utilise comme support pour progresser en autonomie.

Ce projet n’est pas :

- Une API destinée à la production
- Un framework
- Un projet finalisé
- C’est avant tout un support d’apprentissage.

## Ressources et méthode

Ressources utilisées (mises à jour régulièrement) :

- Documentation FastAPI
- Documentation Docker
- Tutoriels open-source / vidéos pédagogiques

Note sur l'IA :  L’IA est utilisée uniquement lorsque je ne parviens pas à trouver la solution par moi-même, afin de privilégier la recherche et la compréhension. 
Aucune génération de code n'est effectuée; l'écriture et l'implémentation sont entièrement manuelles pour garantir une maîtrise complète du projet.
>>>>>>> c834a82436b0f21e95b67cca2e757697af90f45a
