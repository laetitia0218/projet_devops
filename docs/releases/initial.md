# Fiche de mise en production initiale — v1.0.0

* **Date :** 19 novembre 2026
* **Version livrée :** `v1.0.0`
* **Statut :** Déployée en production (Socle initial T5)
* **Responsable de la validation :** L'équipe DevOps (Lead Dev & Développeurs permanents)

---

## 1. Contexte et contenu de la version initiale

Cette première mise en production constitue le **socle technique initial** construit lors de la Partie 1 (T5). Elle remplace l'ancien système défaillant après l'incident d'août (**R3**, **R5**).

### Contenu technique déployé :
* **API REST minimale :**
  * `GET /health` : contrôle de santé renvoyant le statut, la version (`v1.0.0`), le commit Git et l'état de PostgreSQL (**R5**).
  * `GET /products` : consultation du catalogue des produits avec pagination.
  * `POST /orders` : création basique de commandes (sans contrôle de stock dans ce socle initial).
* **Base de données :** PostgreSQL initialisée avec les tables `products` et `orders`.
* **Données initiales :** 1 200 produits générés via `app/seed.py`.
* **Conteneurisation :** Image Docker publiée et exécutée via Docker Compose.

---

## 2. Identification de la version en production (Règle des 10 secondes)

Pour éviter l'erreur de l'incident historique où personne ne savait quelle version tournait (**R5**) :

* **Tag Git :** `v1.0.0`
* **Vérification en direct :**
  ```bash
  curl http://localhost:8000/health
  ```
* **Réponse attendue :**
  ```json
  {
    "status": "ok",
    "version": "v1.0.0",
    "commit": "96ba2ec",
    "database": "connected"
  }
  ```

---

## 3. Risques identifiés & Critères Go / No-Go

* **Risques :**
  * Risque de fuite d'identifiants de base de données (**R4**).
  * Risque de saturation de la base de données lors de l'insertion des 1 200 produits (**R3**).
* **Critères Go / No-Go appliqués :**
  * [x] Tous les tests unitaires passent au vert dans GitHub Actions (**R3**).
  * [x] La route `/health` répond un code `200 OK` en moins de 10 secondes (**R5**).
  * [x] Aucun secret n'est présent dans le code source (**R4**).
  * [x] Les 1 200 produits initiaux sont accessibles via `GET /products`.

---

## 4. Plan de retour arrière (Rollback)

En cas de panne sur cette version initiale :
1. Stopper les conteneurs : `docker-compose down`.
2. Revenir au commit de référence précédent.
3. Délai visé pour le retour arrière : **moins de 5 minutes** (**R5**).
