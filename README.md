# Projet DevOps — Start-up Producteurs & Consommateurs

[![CI Pipeline](https://github.com/laetitia0218/projet_devops/actions/workflows/ci.yml/badge.svg)](https://github.com/laetitia0218/projet_devops/actions/workflows/ci.yml)

Ce dépôt contient l'API minimale et la chaîne CI/CD pour une start-up mettant en relation producteurs, restaurants et particuliers. Ce projet a été construit dans le cadre du **TP DevOps Master 1**.

---

## 📇 Carte Contexte tirée

* **Équipe de développement :** 2 développeurs permanents + 2 alternants (présents 2 semaines sur 4).
* **Contrainte d'effectif :** Pendant les semaines de formation, seuls les 2 permanents assurent la continuité, les revues et la production (**R1**).
* **Attentes des parties prenantes :**
  * **La CEO :** Plus jamais d'incident majeur comme celui d'août (14 heures de blocage un vendredi soir) (**R3**, **R5**).
  * **Le Product Owner :** Nécessité de livrer rapidement des améliorations pour les restaurateurs.
  * **La Lead Dev :** Éviter que les revues de code ne paralysent l'équipe réduite (**R2**).
  * **Le Développeur Freelance :** Payé à l'heure, ne peut pas attendre passivement les validations (**R2**).

---

## 🚀 Démarrage rapide en local

### Prérequis
* Docker & Docker Compose
* *(Optionnel pour tester hors Docker)* : Python 3.11+

### 1. Lancer l'application et la base de données
Cloner le dépôt et lancer les conteneurs (API FastAPI + base PostgreSQL) :

```bash
git clone https://github.com/laetitia0218/projet_devops.git
cd projet_devops

# Lancer la base PostgreSQL et l'API
docker-compose up --build -d
```

L'API est immédiatement disponible sur : **`http://localhost:8000`**

### 2. Peupler la base avec les 1 200 produits initiaux (T5)
Pour charger le jeu de données initial :

```bash
# Exécution du script de données initiales dans le conteneur API
docker-compose exec api python -m app.seed
```

### 3. Lancer les tests unitaires localement

```bash
# Avec Python en local
pytest -v

# Ou directement dans le conteneur
docker-compose exec api pytest -v
```

---

## 📡 Routes de l'API

| Méthode | Route | Description |
|---|---|---|
| `GET` | `/health` | **Règle des 10 secondes (T3)** : renvoie l'état du service, version Git et état PostgreSQL |
| `GET` | `/products?limit=50` | Liste paginée des produits disponibles |
| `PATCH` | `/products/{id}/stock` | **US-42** : déclaration et mise à jour du stock d'un produit par le producteur |
| `POST` | `/orders` | **US-42** : crée une commande avec contrôle de stock et décrémentation atomique |
| `GET` | `/docs` | Documentation interactive Swagger / OpenAPI |

---

## 📚 Documentation du projet

L'ensemble des choix d'architecture et de gouvernance sont consignés dans les livrables suivants :

* **[T1 — Analyse des risques](docs/risques.md)** : identification des 5 risques majeurs (R1 à R5), matrice gravité × effort et priorisation.
* **[T2 — Stratégie de branches](docs/adr/0001-strategie-branches.md)** : ADR validant le choix de GitHub Flow avec déploiement par tag.
* **[T3 — Règles de gestion & Guide de contribution](CONTRIBUTING.md)** : règles de relecture, DoD, format des branches/commits, gestion des secrets et encadrement du freelance.
* **[T3 — Configuration GitHub](docs/config/README.md)** : protection de la branche `main` et environnements.
* **[T4 — Conception du pipeline CI/CD](docs/pipeline.md)** : schéma du pipeline, étapes bloquantes et procédure de retour arrière (< 5 min).
* **[Partie 2 — Découpage US-42 & Livrables de Release](docs/releases/plan-US-42.md)** :
  * [Fiche initiale (v1.0.0)](docs/releases/initial.md)
  * [Plan de réalisation US-42](docs/releases/plan-US-42.md)
  * [Fiche de mise en production (v1.1.0)](docs/releases/v1.1.0.md)
* **[Registre des incidents](docs/incidents.md)** : incident historique d'août et fiches cartes incidents.
