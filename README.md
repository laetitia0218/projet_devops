# Projet DevOps — Start-up Producteurs & Consommateurs

## 📇 Carte Contexte tirée
* **Composition de l'équipe :** 2 développeurs permanents + 2 alternants (présents 2 semaines sur 4).
* **Contrainte d'effectif :** Les semaines de formation, seuls les 2 permanents assurent la production et les revues.
* **Parties prenantes :**
  * **La CEO :** Exige zéro panne majeure (plus jamais un incident comme celui d'août avec 14h de coupure).
  * **Le Product Owner :** Veut des livraisons rapides et fréquentes pour satisfaire les restaurateurs.
  * **La Lead Dev :** S'inquiète du temps passé en relecture de code dans une petite équipe.
  * **Le Développeur Freelance :** Payé à l'heure, refuse d'attendre passivement les revues de code.

---

## 🚀 Démarrage rapide en local

```bash
# Cloner le dépôt
git clone https://github.com/laetitia0218/projet_devops.git
cd projet_devops

# Lancer la stack (API + Base de données PostgreSQL)
docker-compose up --build
```

L'API est accessible sur `http://localhost:8000` (route de santé : `http://localhost:8000/health`).

---

## 📚 Documentation du projet
* [Analyse des risques (T1)](docs/risques.md)
* [Stratégie de branches (T2)](docs/adr/0001-strategie-branches.md)
* [Règles de contribution et gestion (T3)](CONTRIBUTING.md)
* [Configuration GitHub (T3)](docs/config/README.md)
