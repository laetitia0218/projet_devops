# Plan de réalisation — US-42 : Gestion du stock

## 1. User Story

> **En tant que** producteur,  
> **Je veux** déclarer un stock pour chacun de mes produits,  
> **Afin qu'** une commande qui dépasse ce stock soit refusée avec un message clair.

* **Contrainte de mise en production :** Possibilité de retour arrière vers la version précédente en **moins de 5 minutes** (**R5**).
* **Version cible visée :** `v1.1.0` (incrément mineur : nouvelle fonctionnalité rétrocompatible).

---

## 2. Découpage en tâches et répartition dans l'équipe

Pour respecter les exigences du TP et nos règles de gestion ([`CONTRIBUTING.md`](../../CONTRIBUTING.md)), la User Story est découpée en 3 tâches principales avec une répartition claire entre les membres du trinôme :

| N° | Tâche | Description technique | Responsable | Branche dédiée |
|---|---|---|---|---|
| **Tâche 1** | **Mise à jour du stock** | Ajout de l'endpoint `PATCH /products/{id}/stock` permettant au producteur de déclarer ou modifier la quantité disponible en stock. | Développeur 1 (Laetitia) | `feat/US-42-declaration-stock` |
| **Tâche 2** | **Contrôle et décrémentation du stock** | Modification de `POST /orders` pour vérifier le stock disponible en base : refus avec HTTP 400 et message explicite si commande > stock, et décrémentation automatique en cas de succès. | Développeur 2 (Zakaria) | `feat/US-42-validation-commandes` |
| **Tâche 3** | **Tests et pipeline CI/CD** | Ajout des tests automatisés (cas passant, cas stock insuffisant) et adaptation du workflow GitHub Actions (tests + build image Docker). | Équipe DevOps / Lead Dev | `feat/US-42-tests-et-pipeline` |

---

## 3. Critères d'acceptation (Acceptance Criteria)

1. **Déclaration du stock :**
   * L'appel `PATCH /products/{id}/stock` avec le corps `{"stock": 45}` met à jour le stock du produit ciblé.
   * Si le produit n'existe pas, l'API renvoie un code `404 Not Found`.
   * Si le stock déclaré est négatif (`stock < 0`), l'API renvoie une erreur `400 Bad Request`.

2. **Validation des commandes :**
   * Lorsqu'une commande est passée avec une quantité inférieure ou égale au stock disponible :
     * La commande est créée (`201 Created`).
     * Le stock du produit est décrémenté du montant commandé.
   * Lorsqu'une commande demande une quantité strictement supérieure au stock disponible :
     * La commande est **refusée** (`400 Bad Request`).
     * Un message d'erreur clair et explicite est renvoyé en JSON :
       ```json
       {
         "detail": "Stock insuffisant : quantite demandee (10) superieure au stock disponible (4)."
       }
       ```
     * Aucun enregistrement n'est inséré dans la table `orders`.

3. **Règle des 10 secondes et versionnage :**
   * La route `GET /health` renvoie la nouvelle version `v1.1.0` (**R5**).

---

## 4. Stratégie de branches et processus de livraison

Conformément à notre ADR [`docs/adr/0001-strategie-branches.md`](../adr/0001-strategie-branches.md) et notre guide [`CONTRIBUTING.md`](../../CONTRIBUTING.md) :

1. Chaque tâche est développée sur sa branche isolée.
2. Une Pull Request est ouverte vers `main` pour chaque tâche.
3. Chaque PR doit obtenir :
   * Le passage au vert des tests automatiques dans GitHub Actions (**R3**).
   * **1 approbation obligatoire** d'un autre membre de l'équipe (**R1**, **R2**).
4. Fusion dans `main` via **Squash and merge**.
5. Une fois toutes les tâches intégrées sur `main`, création du tag Git de release `v1.1.0` et rédaction de la fiche de mise en production [`docs/releases/v1.1.0.md`](v1.1.0.md).
