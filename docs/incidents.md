# Registre des Incidents (docs/incidents.md)

Ce document consigne les incidents survenus sur la plateforme, les décisions prises par l'équipe, les règles appliquées ou enfreintes, ainsi que les adaptations apportées à nos règles de gestion ([`CONTRIBUTING.md`](../CONTRIBUTING.md)).

---

## Incident Fondateur — Panne du mois d'août (Historique)

* **Date :** Août 2026, un vendredi à 19 h
* **Durée de l'interruption :** 14 heures en pleine saison touristique
* **Symptômes :** Les commandes étaient totalement bloquées sur le site, version en production inconnue de l'équipe.
* **Causes racines :**
  1. Push direct sur la branche principale sans revue ni tests (**R2**, **R3**).
  2. Déploiement automatique en SSH avec le tag `latest` rendant impossible l'identification de la version active (**R5**).
  3. Déploiement réalisé un vendredi soir à 19 h en dehors des heures de présence de l'équipe (**R3**).
  4. Absence de procédure de rollback testée (**R5**).
* **Décisions & Règles mises en place en réponse :**
  * Interdiction absolue des pushs directs sur `main` via la protection de branche GitHub (**R2**).
  * 1 revue de code obligatoire avant toute fusion (**R1**, **R2**).
  * Bannissement du tag `latest` au profit de tags sémantiques `vX.Y.Z` (**R5**).
  * Ajout de la route `/health` pour identifier la version en moins de 10 secondes (**R5**).
  * Gel des déploiements le vendredi à partir de 14 h jusqu'au lundi matin (**R3**).
  * Démonstration d'une procédure de rollback applicatif en moins de 5 minutes (**R5**).

---

## Modèle de fiche pour Carte Incident (Bonus Enseignant)

Lorsqu'une carte incident est distribuée par l'enseignant durant la séance, remplir la section ci-dessous :

### Fiche Incident : [Nom de la carte incident]
* **Date & Heure :** 
* **Carte tirée :** 
* **Description de l'incident :** 
* **Décision prise par l'équipe :** 
* **Règle appliquée ou enfreinte (justification) :** 
* **Temps de résolution :** 
* **Évolution de nos règles en conséquence :** 
